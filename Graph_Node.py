class Graph_Node(object):

    def __init__(self, new_name):
        self.name = new_name
        self.neighbors = []
        self.read = False

    def __str__(self):
        return self.name

    def add_neighbor(self, adj_name, dist):
        self.neighbors.append([adj_name,int(dist)])

    def dist_from(self, adj_name):
        for adj in self.neighbors:
            if adj[0] == adj_name:
                return adj[1]
        return -1

    def read(self):
        self.read = False

    def is_read(self ):
        return self.read

    def clear_read(self):
        self.read = True

    def get_name(self):
        return self.name

    def get_neighbors(self):
        return self.neighbors

    def shortest_neighbor(self):
        min_ind = 0
        for x in range(1,len(neighbors)):
            if neighbors[x][1] < neighbors[min_ind][1]:
                min_ind = x
        return neighbors[min_ind][0]

    def all_neighbors(self):
        all = []
        for neighbor in self.neighbors:
            all.append(neighbor[0].name)
        all.sort()
        return all
