input = "testIn"
#input = "D7input.txt"

instr = open(input, "r").readlines()
wires = []
signals = []

def get_hex_signal(signal):
    return list("{0:b}".format(signal).rjust(16, '0'))

def get_hex_string(signal):
    str = ''
    for x in signal:
        str += x
    return str

def get_dec(signal):
    str = get_hex_string(signal)
    return int(str,2)

def new_blank():
    temp = []
    for x in range(0,16):
        temp.append('0')
    return temp

def opposite(sig):
    opp = new_blank()
    for x in range(0,16):
        opp[x] = '1' if sig[x] == '0' else '0'
    return opp

def assign(wire, signal):
    global wires
    global signals
    if wire in wires:
        signals[wires.index(wire)] = signal
    else:
        wires.append(wire)
        signals.append(signal)

def compliment(sent, reciev):
    global wires
    global signals
    if sent in wires:
        in_s = wires.index(sent)
        to_send = opposite(signals[in_s])
        if reciev in wires:
            in_r = wires.index(reciev)
            signals[in_r] = to_send
        else:
            wires.append(reciev)
            signals.append(to_send)
    else:
        wires.append(sent)
        signals.append(new_blank())
        to_send = opposite(new_blank())
        if reciev in wires:
            in_r = wires.index(reciev)
            signals[in_r] = to_send
        else:
            wires.append(reciev)
            signals.append(to_send)

def get_sig(wire):
    global wires
    global signals
    if wire not in wires:
        wires.append(wire)
        signals.append(new_blank)
    ind = wires.index(wire)
    return signals[ind]

def overlap(w1, w2):
    new_sig = new_blank()
    for x in range(0,16):
        if w1[x] == '1' and w2[x] == '1':
            new_sig[x] = '1'
    return new_sig

def combine(w1,w2):
    new_sig = new_blank()
    for x in range(0,16):
        if w1[x] == '1' or w2[x] == '1':
            new_sig[x] = '1'
    return new_sig

def shftL(sig, amnt):
    temp = sig
    for x in range (0, amnt):
        for y in range(1, 16):
            temp[y-1] = temp[y]
        temp[15] = '0'
        print temp
    return temp

def shftR(sig, amnt):
    temp = sig
    for x in range(0,amnt):
        for y in range(1,16):
            temp[y] = temp[y-1]
        temp[0] = '0'
    return temp

'''
000 -> xx
NOT xx -> xx
xx AND xx -> xx
xx OR xx -> xx
xx LSHIFT xx -> xx
xx RSHIFT xx -> xx
'''
def parse_line(line):
    curr = line.split()
    if curr[1] == "->":
        sig = int(curr[0])
        assign(curr[2],get_hex_signal(sig))
    elif curr[0] == "NOT":
        compliment(curr[1],curr[3])
    elif curr[1] == "AND":
        ovrlp = overlap(get_sig(curr[0]),get_sig(curr[2]))
        assign(curr[4],ovrlp)
    elif curr[1] == "OR":
        comb = combine(get_sig(curr[0]),get_sig(curr[2]))
        assign(curr[4],comb)
    elif curr[1] == "LSHIFT":
        lShift = shftL(get_sig(curr[0]),int(curr[2]))
        assign(curr[4], lShift)
    elif curr[1] == "RSHIFT":
        rShift = shftR(get_sig(curr[0]),int(curr[2]))
        assign(curr[4], rShift)

for line in instr:
    parse_line(line)

print ''
for wire in wires:
    sig = wires.index(wire)
    print wire, ": ", get_dec(signals[sig])
