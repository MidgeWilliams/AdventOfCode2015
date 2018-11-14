'''
Everything but NOT works...
'''

#str = "testIn"
str = "D7input.txt"
instr = open(str,'r').readlines()

wires = []
binsig_arr = []
binsig_str = []



#Given signal (string)
def get_bin_arr(signal):
    return list(signal)

#Given signal (array)
def get_bin_str(signal):
    str = ''
    for x in range(0,len(signal)):
        str += signal[x]
    return str

#Given decimal string of signal
def get_new_bin_str(dec_sig):
    return "{0:b}".format(int(dec_sig)).rjust(16, '0')

#Returns the dec int value give string bin
def get_dec(signal):
    return int(signal,2)

def get_blank_str():
    return "0000000000000000"

def get_blank_arr():
    temp = []
    for x in range(0,16):
        temp.append('0')
    return temp

def trim_wire(wire):
    str = wire
    if wire[len(wire)-1] == "\n":
        str = wire[0:len(wire)-1]
    return str

def new_wire(wire):
    global wires
    global binsig_arr
    global binsig_str
    wires.append(wire)
    binsig_str.append(get_blank_str())
    binsig_arr.append(get_blank_arr())

def get_wire_ind(wire):
    global wires
    wire = trim_wire(wire)
    if wire not in wires:
        new_wire(wire)
    return wires.index(wire)

def wire_toString(wire):
    global binsig_str
    ind = get_wire_ind(wire)
    return "%s: %d" %(wire,get_dec(binsig_str[ind]))

#Given wire name & signal (string)
def assign(wire, signal):
    global binsig_arr
    global binsig_str
    ind = get_wire_ind(wire)
    binsig_str[ind] = signal
    binsig_arr[ind] = get_bin_arr(signal)


#Given wire, returns string signal
def opposite(wire):
    global binsig_arr
    ind = get_wire_ind(wire)
    cur = binsig_arr[ind]
    temp = get_blank_arr()
    for x in range(0,16):
        temp[x] = '1' if cur[x] == '0' else '0'
    return get_bin_str(temp)

#Given two wires, returns string signal
def intersect(wire1,wire2):
    global binsig_arr
    ind1 = get_wire_ind(wire1)
    sig1 = binsig_arr[ind1]
    ind2 = get_wire_ind(wire2)
    sig2 = binsig_arr[ind2]
    temp = get_blank_arr()
    for x in range (0,16):
        if sig1[x] == '1' and sig2[x] == '1':
            temp[x] = '1'
    return get_bin_str(temp)

#Given two wires, returns string signal
def union(wire1, wire2):
    global binsig_arr
    ind1 = get_wire_ind(wire1)
    sig1 = binsig_arr[ind1]
    ind2 = get_wire_ind(wire2)
    sig2 = binsig_arr[ind2]
    temp = get_blank_arr()
    for x in range (0,16):
        if sig1[x] == '1' or sig2[x] == '1':
            temp[x] = '1'
    return get_bin_str(temp)

def lShift(wire, rep):
    global binsig_arr
    ind = get_wire_ind(wire)
    temp = binsig_arr[ind]
    for i in range(0,int(rep)):
        for x in range(1,16):
            temp[x-1] = temp[x]
        temp[15] = '0'
    return get_bin_str(temp)

def rShift(wire, rep):
    global binsig_arr
    ind = get_wire_ind(wire)
    temp = binsig_arr[ind]
    for i in range(0,int(rep)):
        for x in range(15,1,-1):
            temp[x] = temp[x-1]
        temp[0] = '0'
    return get_bin_str(temp)

def alphabetize():
    global wires
    all_str = []
    for wire in wires:
        all_str.append(wire_toString(wire))
    all_str.sort()
    return all_str

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
    if cur[0] == "NOT":
        sig = opposite(cur[1])
        assign(cur[3],sig)
    elif cur[1] == '->':
        sig = get_new_bin_str(cur[0])
        assign(cur[2],sig)
    elif cur[1] == 'AND':
        sig = intersect(cur[0],cur[2])
        assign(cur[4],sig)
    elif cur[1] == 'OR':
        sig = union(cur[0],cur[2])
        assign(cur[4],sig)
    elif cur[1] == "LSHIFT":
        sig = lShift(cur[0],cur[2])
        assign(cur[4],sig)
    elif cur[1] == "RSHIFT":
        sig = rShift(cur[0],cur[2])
        assign(cur[4],sig)

for line in instr:
    process_line(line)

new_wires = alphabetize()
for line in new_wires:
    print line
