file_name = 'D12.txt'
input = open(file_name,'r').read()
#input = '{"a":{"b":4},"c":-1}'

segments = [input]

non_digs = ['[',']','{','}',':',"\"",',']

def fix_segs():
    global segments
    temp = []
    for seg in segments:
        if type(seg) == list:
            for each in seg:
                if each != '' and each !='\n': temp.append(each)
    segments = temp

def split(thing):
    global segments
    lng = len(segments)
    for x in range(0,lng):
        segments[x] = segments[x].split(thing)
    fix_segs()

def split_all():
    global non_digs
    a = ord('a')
    for x in range(a,a+26):
        cur = chr(x)
        split(cur)

    for dig in non_digs:
        split(dig)

def sum():
    global segments
    sum = 0
    for each in segments:
        sum += int(each)
    return sum


split_all()
print sum()
