input = open('input.txt','r').read()
#result = open('result.txt', 'r').read()
#print input==result
result = ''
floor = 0

part2 = False #Set to false to get result of part1

for x in range(0, len(input)):
    result += input[x]
    if input[x] == "(":
        floor += 1
    elif input[x] == ")":
        floor -= 1
    if part2:
        if floor < 0:
            print x + 1
            break
if part2 == False:
    print floor
