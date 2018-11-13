part1 = True

def fix_last(last):
    lgth = len(last)
    return last[0:lgth-1]

def get_side(line, side):
    allSides = line.split('x')
    allSides[2] = fix_last(allSides[2])
    return int(allSides[side])

def get_extra(line):
    l = get_side(line, 0)
    w = get_side(line, 1)
    h = get_side(line, 2)

    small = 0
    if min(l, w, h) == l:
        if min(w, h) == w:
            small = l*w
        else:
            small = l*h
    elif min(l,w,h) == w:
        if min(l,h) == l:
            small = w*l
        else:
            small = w*h
    elif min(l,w,h) == h:
        if min(l,w) == l:
            small = h*l
        else:
            small = h*w

    return small

def get_Surface(line):
    lh = 2*get_side(line, 0)*get_side(line, 1)
    hw = 2*get_side(line, 1)*get_side(line, 2)
    wl = 2*get_side(line, 2)*get_side(line, 0)
    return lh+hw+wl+get_extra(line)


total = 0

with open("inputD2", "r") as file:
    for line in file:
        if part1:
            total += get_Surface(line)

print total
