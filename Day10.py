start = '1321131112'
#start = '1' #WANT: 312211


def process_num(given):
    str = ""
    while len(given) > 1:
        first = int(given[0])
        i = 1

        while i < len(given) and first == int(given[i]):
            i+=1
        str += "%d%d"%(i,first)
        given = given[i:len(given)]

    if len(given) == 1:
        str += "%d%d"%(1,int(given[0]))
    return str


for x in range(0,50):
    start = process_num(start)
    print len(start)
print start, "\n", len(start)
