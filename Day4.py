import hashlib

key = "bgvyzdsv"
want = "000000"

def combKey(num):
    global key
    return "%s%d" % (key,num)

search = True
i = 1
while search:
    cur = combKey(i)
    #print cur, "     ",
    hash = hashlib.md5(cur.encode()).hexdigest()
    #print hash[0:5]
    if len(hash) > 5 and hash[0:6] == want:
        search = False
        print key, i
    i += 1

# Want: abcdef609043
