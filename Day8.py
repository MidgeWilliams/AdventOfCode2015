#str = "testIn"
str = "D8input.txt"
input = open(str, "r").readlines()
part1 = False

def trim_new_line(line):
    if line[len(line)-1] == "\n":
        return line[0:len(line)-1]
    return line

def total_length(line):
    cur = line
    cur = trim_new_line(line)
    print cur, "(%d) --> "%(len(cur)),
    return len(cur)

def doub_bs(line):
    global part1
    cur = line
    str = "\\\\"
    if part1:
        while str in cur:
            ind = cur.index(str)
            cur = cur[0:ind] + 'X' + cur[ind+2:len(cur)]
    else:
        while str in cur:
            ind = cur.index(str)
            cur = cur[0:ind] + 'XXXX' + cur[ind+2:len(cur)]
    return cur

def quote(line):
    global part1
    cur = line
    str = "\\\""
    if part1:
        while str in cur:
            ind = cur.index(str)
            cur = cur[0:ind] + cur[ind+1:len(cur)]
    else:
        temp = cur
        while str in temp:
            ind = temp.index(str)
            temp = temp[ind+2:len(cur)]
            cur += "XX"
    return cur

def x_escape(line):
    global part1
    cur = line
    str = "\\x"
    if part1:
        while str in cur:
            ind = cur.index(str)
            cur = cur[0:ind] + cur[ind+3:len(cur)]
    else:
        temp = cur
        while str in temp:
            ind = temp.index(str)
            temp = temp[ind+3:len(cur)]
            cur += "X"
    return cur

def string_length(line):
    global part1
    cur = trim_new_line(line)
    if part1: cur = cur[1:len(cur)-1] #Takes away quotes
    cur = doub_bs(cur)
    cur = quote(cur)
    cur = x_escape(cur)
    if not part1: cur = "XX" + cur + "XX"
    print cur, "(%d)"%(len(cur))
    return len(cur)

def process_line(line):
    count = []
    count.append(total_length(line))
    count.append(string_length(line))

    return count

total_char = 0
total_str = 0
for line in input:
    cur = process_line(line)
    total_char += cur[0]
    total_str += cur[1]

if not part1: print total_str, " - ", total_char, " = ", total_str - total_char
if part1: print total_char, " - ", total_str, " = ", total_char - total_str
