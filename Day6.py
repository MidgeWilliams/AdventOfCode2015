#file = "testIn"
file = "D6input.txt"
instruc = open(file, "r").readlines()

lights = []
size = 1000

for x in range(0,size):#Change to 1000 when time
    temp = []
    for y in range(0,size):
        temp.append(0)
    lights.append(temp)

def get_ranges(s,f):
    temp = []
    for x in range(int(s),int(f)+1):
        temp.append(x)
    return temp

def turn_on(x_val, y_val):
    global lights
    for x in x_val:
        for y in y_val:
            lights[x][y] += 1

def turn_off(x_val,y_val):
    global lights
    for x in x_val:
        for y in y_val:
            if lights[x][y] != 0: lights[x][y] -= 1 

def toggle(x_val,y_val):
    global lights
    for x in x_val:
        for y in y_val:
            lights[x][y] += 2

def process_cmd(line):
    curr = line.split(" ")
    if curr[0] == "toggle":
        s = curr[1].split(",")
        f = curr[3].split(",")
        x_val = get_ranges(s[0],f[0])
        y_val = get_ranges(s[1],f[1])
        toggle(x_val,y_val)
    elif curr[1] == "on":
        s = curr[2].split(",")
        f = curr[4].split(",")
        x_val = get_ranges(s[0],f[0])
        y_val = get_ranges(s[1],f[1])
        turn_on(x_val, y_val)
    elif curr[1] == "off":
        s = curr[2].split(",")
        f = curr[4].split(",")
        x_val = get_ranges(s[0],f[0])
        y_val = get_ranges(s[1],f[1])
        turn_off(x_val,y_val)

def how_many_on():
    tot_br = 0
    for row in lights:
        for light in row:
            tot_br += light
    return tot_br

def print_lights():
    global lights
    for row in lights:
        print row

for line in instruc:
    process_cmd(line)

#print_lights()

print "Brightness is ", how_many_on()
