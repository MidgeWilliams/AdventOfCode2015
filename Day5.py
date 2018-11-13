input = open("D5input.txt","r").readlines()
#input = open("testIn", "r").readlines()
part1 = False
vowels = ['a','i','e', 'o', 'u']

def check_disallowed(line):
    if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
        #print "had disallowed   ",
        return False
    #print "had no disallowed   ",
    return True

def check_vowels(line):
    global vowels
    curr = list(line)
    inclVowels = []
    for i in curr:
        if i in vowels:
            inclVowels.append(i)
    #print "had vowels ", inclVowels, "   ",
    return len(inclVowels) > 2


def check_double(line):
    for x in range(1, len(line)):
        if line[x] == line[x-1]:
            #print "had double letters ", line[x], line[x-1], "\n"
            return True
    #print "No double letters\n"
    return False

def check_Sep_by1(line):
    for x in range(2, len(line)):
        if line[x] == line[x-2]:
            return True
    return False

def check_pair_repeat(line):
    for x in range(1, len(line)):
        pair = line[x-1:x+1]
        temp1 = line[0:x-1]
        temp2 = line[x+1:len(line)]
        if pair in temp1 or pair in temp2:
            return True
    return False


def check_good(line):
    if part1:
        return check_disallowed(line) and check_vowels(line) and check_double(line)
    else:
        return check_Sep_by1(line) and check_pair_repeat(line)


nice = 0
total = 0

for line in input:
    line = line[0:len(line)-1]
    #print line, ":  ",
    if check_good(line):
        nice += 1
    total += 1

print nice, " out of ", total, " are Nice"
