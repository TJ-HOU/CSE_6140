import networkx as nx

"""
A function that reads in a file and converts it into a graph using networkx
"""

def makegraph(filename):
    graphfile = open(filename,'r')
    lines = graphfile.readlines()
    Vnum,Enum,n = lines[0].split()
    G = nx.Graph()
    for i, line in enumerate(lines):
        if i != 0:
            vals = line.split()
            for j in vals:
                G.add_edge(int(i),int(j))
    return G
