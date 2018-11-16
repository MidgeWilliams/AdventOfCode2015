
from Graph_Node import Graph_Node

part2 = True
#str = 'testIn'
str = 'D9input.txt'

input = open(str, 'r').readlines()

places = []
paths = []

def trim_new_line(line):
    if "\n" in line:
        line = line[0:len(line)-1]
    return line

def get_place(name):
    global places
    for place in places:
        if place.get_name() == name:
            return place
    new_place = Graph_Node(name)
    places.append(new_place)
    return new_place

def add_dist(place1, place2, dist):
    place1.add_neighbor(place2, dist)
    place2.add_neighbor(place1, dist)

def process_line(line):
    cur = trim_new_line(line).split(" ")
    place1 = get_place(cur[0])
    place2 = get_place(cur[2])
    add_dist(place1, place2, int(cur[4]))

def transfer_path(path):
    global paths
    cur = []
    for thing in path:
        cur.append(thing)
    paths.append(cur)

def make_orders(read, unread):
    global paths
    if len(unread) != 0:
        left = len(unread)
        cur_read = read
        cur_unrd = unread
        for x in range(0,left):
            cur = cur_unrd[0]
            cur_read.append(cur)
            cur_unrd.remove(cur)
            make_orders(cur_read,cur_unrd)
            cur_read.remove(cur)
            cur_unrd.append(cur)
    else:
        transfer_path(read)

def get_path_length(path):
    dist = 0
    for x in range(1,len(path)):
        dist += path[x-1].dist_from(path[x])
    return dist

for line in input:
    process_line(line)


make_orders([],places)
distances = []
for path in paths:
    distances.append(get_path_length(path))
distances.sort()
if part2:
    distances.reverse()
print distances[0]
