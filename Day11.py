input = 'vzbxkghb'
#input = 'ghijklmn' #Want ghjaabcc
#input = 'abcdefgh' #Want abcdffaa

letters = []
values = []

def make_lists():
    global input,letters,values
    letters = list(input)
    for letter in letters:
        values.append(ord(letter))

def string_from_list():
    global letters
    str = ""
    for letter in letters:
        str += letter
    return str

def poss_doub():
    doubs = []
    for x in range(0,26):
        asc = ord('a') + x
        char = chr(asc)
        doubs.append(char+char)
    return doubs

def remove(password,str):
    ind = password.index(str)
    password = password[0:ind]+password[ind+1:len(password)]
    return password

# Needs to have consecutive chars
def rule_1():
    global values
    for x in range(2,len(values)):
        if values[x-2] + 1 == values[x-1] and values[x-1] +1 == values[x]:
            return True
    return False

# Can't have the letters: i, o, l
def rule_2():
    global letters
    if 'i' in letters or 'o' in letters or 'l' in letters:
        return False
    return True

# Needs two non overlapping double letters
def rule_3():
    password = string_from_list()
    doubs = poss_doub()
    i = 0
    for doub in doubs:
        if doub in password:
            i += 1
            password = remove(password,doub)
        if i == 2:
            return True
    return False

def fix_letters():
    global letters,values
    for x in range(0,len(values)):
        letters[x] = chr(values[x])

def increment():
    global values
    cur_ind = len(values)-1
    values[cur_ind] += 1
    while values[cur_ind] > ord('z'):
        values[cur_ind] = ord('a')
        cur_ind -= 1
        values[cur_ind] += 1
    fix_letters()


make_lists()
for x in range (0,2):
    not_valid = True

    while not_valid:
        increment()
        not_valid = not (rule_1() and rule_2() and rule_3())
    input = string_from_list()
    print input
#vzbxxyzz first one
