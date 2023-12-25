import networkx as nx
import os
import sys

def part1():
    g = nx.Graph()

    for line in open(os.path.join(sys.path[0], 'day25.txt')):
        left, right = line.split(":")
        for node in right.strip().split():
            g.add_edge(left, node)

    g.remove_edges_from(nx.minimum_edge_cut(g))
    a, b = nx.connected_components(g)

    print(len(a) * len(b))

if __name__ == '__main__':
    part1()