paper = False

# Fixes the last side length by taking away "\n"
def fix_last(last):
    lgth = len(last)
    return last[0:lgth-1]

# Gets a side length given the line and which side (0-2)
def get_side(line, side):
    allSides = line.split('x')
    allSides[2] = fix_last(allSides[2])
    return int(allSides[side])

# Gets extra, finds smallest 2 sides and does the appropriate operation with
# them
def get_extra(line):
    l = get_side(line, 0)
    w = get_side(line, 1)
    h = get_side(line, 2)

    small = 0
    if min(l, w, h) == l:
        if min(w, h) == w:
            small = do_with_smallest(l,w)
        else:
            small = do_with_smallest(l,h)
    elif min(l,w,h) == w:
        if min(l,h) == l:
            small = do_with_smallest(w,l)
        else:
            small = do_with_smallest(w,h)
    elif min(l,w,h) == h:
        if min(l,w) == l:
            small = do_with_smallest(h,l)
        else:
            small = do_with_smallest(h,w)

    return small

# Returns area of two sides if finding paper, returns the sum of double both
# for ribbon
def do_with_smallest(side_1, side_2):
    if paper:
        return side_1*side_2
    else:
        print side_1, " ", side_2
        return 2*side_1+2*side_2

# Gets surface area plus extra
def get_Surface(line):
    global paper
    paper = True
    lh = 2*get_side(line, 0)*get_side(line, 1)
    hw = 2*get_side(line, 1)*get_side(line, 2)
    wl = 2*get_side(line, 2)*get_side(line, 0)
    return lh+hw+wl+get_extra(line)

# Gets the length of ribbon for the bow
def get_Bow(line):
    return get_side(line, 0)*get_side(line, 1)*get_side(line, 2)

# Gets the length of ribbon needed
def get_Ribbon(line):
    global paper
    paper = False
    return get_Bow(line) + get_extra(line)

total_paper = 0
total_ribbon = 0

with open("inputD2", "r") as file:
    for line in file:
        total_paper += get_Surface(line)
        print get_Ribbon(line)
        total_ribbon += get_Ribbon(line)


print "Amount of wrapping paper: ", total_paper
print "Amount of ribbon:         ", total_ribbon
