#str = 'testIn'
str = 'D7input.txt'

instruc = open(str, 'r').readlines()

wires = []
signals = []

def hasSignal(wire):
    global wires
    if wire.isdigit():
        return True
    return True if wire in wires else False

def alphabetize():
    global wires
    global signals
    temp = []
    for x in range(0,len(wires)):
        str = "%s: %d" % (wires[x],signals[x])
        temp.append(str)
    temp.sort()
    return temp

def getSignal(wire):
    global signals
    if wire.isdigit():
        return int(wire)
    else:
        ind = getWireInd(wire)
        return signals[ind]

def trimWire(wire):
    str = wire
    if wire[len(wire)-1] == '\n':
        str = wire[0:len(wire)-1]
    return str

def getWireInd(wire):
    global wires
    if wire.isdigit():
        return -1
    else:
        wire = trimWire(wire)
        if wire not in wires:
            wires.append(wire)
            signals.append(0)
        return wires.index(wire)

def assign(wire,sig):
    global signals
    ind = getWireInd(wire)
    signals[ind] = int(sig)

def opposite(wire):
    global signals
    cur = getSignal(wire)
    return ~cur

def intersection(wire1,wire2):
    global signals
    sig1 = getSignal(wire1)
    sig2 = getSignal(wire2)

    return sig1 & sig2

def union(wire1,wire2):
    global signals
    sig1 = getSignal(wire1)
    sig2 = getSignal(wire2)

    return sig1 | sig2

def lShift(wire, rep):
    global signals
    sig = getSignal(wire)
    return sig << int(rep)

def rShift(wire, rep):
    global signals
    sig = getSignal(wire)
    return sig >> int(rep)

'''
NOT xx -> xx
000 -> xx
xx AND xx -> xx
xx OR xx -> xx
xx LSHIFT xx -> xx
xx RSHIFT xx -> xx
'''
def process_line(line):
    cur = line.split(' ')
    if cur[0] == 'NOT' and hasSignal(cur[1]):
        sig = opposite(cur[1])
        assign(cur[3],sig)
        return True
    elif cur[1] == '->':
        if cur[0].isdigit():
            assign(cur[2],cur[0])
            return True
        elif hasSignal(cur[0]):
            sig = getSignal(cur[0])
            assign(cur[2],sig)
            return True
    elif cur[1] == 'AND' and hasSignal(cur[0]) and hasSignal(cur[2]):
        sig = intersection(cur[0],cur[2])
        assign(cur[4],sig)
        return True
    elif cur[1] == 'OR' and hasSignal(cur[0]) and hasSignal(cur[2]):
        sig = union(cur[0],cur[2])
        assign(cur[4],sig)
        return True
    elif cur[1] == 'LSHIFT' and hasSignal(cur[0]):
        sig = lShift(cur[0], cur[2])
        assign(cur[4],sig)
        return True
    elif cur[1] == 'RSHIFT' and hasSignal(cur[0]):
        sig = rShift(cur[0], cur[2])
        assign(cur[4],sig)
        return True
    return False

while len(instruc) > 0:
    cur = instruc.pop(0)
    if not process_line(cur):
        instruc.append(cur)


new_wires = alphabetize()
for line in new_wires:
    print line
