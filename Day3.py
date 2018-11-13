dir = open("D3input.txt", "r").read()
#dir = open("testIn", "r").read()
s_coor = [0,0]
r_coor = [0,0]

def cur_place(coor):
    return "%d, %d" % (coor[0], coor[1])

s_visited = set([cur_place(s_coor)])
r_visited = set([cur_place(r_coor)])

def update_pos(next, coor):
    if next == '^':
        coor[1] += 1
    elif next == '>':
        coor[0] += 1
    elif next == 'v':
        coor[1] -= 1
    elif next == '<':
        coor[0] -= 1
    return coor

for z in range(0, len(dir)):
    if z % 2 == 0:
        s_coor = update_pos(dir[z], s_coor)
        if (cur_place(s_coor) in s_visited) == False:
            s_visited.add(cur_place(s_coor))
    else:
        r_coor = update_pos(dir[z], r_coor)
        if (cur_place(r_coor) in r_visited) == False:
            r_visited.add(cur_place(r_coor))

print len(s_visited|r_visited)
