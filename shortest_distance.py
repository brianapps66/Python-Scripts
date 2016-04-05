import re
import itertools
from collections import defaultdict

file = open('distances.txt', 'r').read().splitlines()


def format_file(file):
    l = [sum((re.findall(r'^\w+', line),
              re.findall(r'^(?=.*\b)(?:\S+ ){2}(\S+)', line),
              re.findall(r'(\w+)$', line)), []) for
         line in file]
    print(l)

    for i in range(len(l)):
        a = l[i][0]
        b = l[i][1]
        c = l[i][2]

    return l

import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def __lt__(self, other):
        return (self.id < other.id)

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_neighbor_distance(self, neighbor):
        return self.adjacent[neighbor]

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str(
            [x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


def shortest(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start, target):
    print(
        '''Dijkstra's shortest path''')
    start.set_distance(0)

    unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    print(unvisited_queue)
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()
        for next in current.adjacent:
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print('updated : current = %s next = %s new_dist = %s' % (
                    current.get_id(), next.get_id(), next.get_distance()))
            else:
                print('not updated : current = %s next = %s new_dist = %s' % (
                    current.get_id(), next.get_id(), next.get_distance()))

        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if
                           not v.visited]
        heapq.heapify(unvisited_queue)


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.get_vertex(start):
        return []
    paths = []
    for node in graph.get_vertices():
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def get_distance(graph, start, end):
    pass


if __name__ == '__main__':

    g = Graph()
    l = format_file(file)
    for i in range(len(l)):
        if g.get_vertex(l[i][0]) == None:
            print(l[i][0])
            g.add_vertex(l[i][0])
            if g.get_vertex(l[i][1]) == None:
                print(l[i][1])
                g.add_vertex(l[i][1])

    for item in l:
        print(item[0], item[1], item[2])
        edge = item[0], item[1], item[2]
        g.add_edge(item[0], item[1], int(item[2]))

    print('Graph data:')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))

    dijkstra(g, g.get_vertex('Faerun'), g.get_vertex('Norrath'))
    visited = []

    start_end = itertools.combinations(g.get_vertices(), 2)
    a = []
    for i in start_end:
        a.append(i)
    print('find all graphs: ', a, '\nLength = ', len(a))

    print('distance: ',
          g.get_vertex('Norrath').get_neighbor_distance(g.vert_dict['Faerun']))
    with open('distances.txt') as f:
        data = f.read()

    distances = defaultdict(dict)
    for source, dest, distance in re.findall('(\w+) to (\w+) = (\d+)', data):
        distances[source][dest] = int(distance)
        distances[dest][source] = int(distance)

    shortest_path, longest_path = None, None
    shortest_distance, longest_distance = None, None
    for path in itertools.permutations(distances.keys()):
        curr = 0
        for source, dest in zip(path, path[1:]):
            curr += distances[source][dest]
        if not shortest_distance or curr < shortest_distance:
            shortest_path, shortest_distance = path, curr
        if not longest_distance or curr > longest_distance:
            longest_path, longest_distance = path, curr

    print(shortest_distance, longest_distance)
    print(shortest_path)
    print(longest_path)
