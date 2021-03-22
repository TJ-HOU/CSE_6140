import heapq
import sys
#import networkx as nx
#import time
def computeMST(G):

    # computes weight of MST
    totalweight = 0

    # priority queue delcaration
    pq = [] 
    
    src = 0

    """
    key     : int list containing the weights of edges
    parent  : int list containing the parent of each node
    inMST   : boolean list that says if a node is in the MST

    """
    key = []
    parent = []
    inMST = []
    for i in range(0,len(G)):
        key.append(sys.maxint)
        parent.append(-1)
        inMST.append(False)

    # establishes pq as a heap then adds the first node to it
    heapq.heappush(pq,(0,src))

    # makes weight of first node 0
    key[src] = 0

    # while the priority queue isn't empty this runs
    while(len(pq) != 0):

        # uses priority queue grab node with smallest weight 
        u = heapq.heappop(pq)[1]
        inMST[u] = True

        # checks all of neighbors of node as candidates for MST
        for i in G.neighbors(u):
            v = i
            weight = sys.maxint
            # since some are multigraphs, this finds edge 
            # between u and v of minimum weight
            for j in G[u][v]:
                if (G[u][v][j]['weight'] < weight):
                    weight = G[u][v][j]['weight']

            if (inMST[v] == False and key[v] > weight):
                key[v] = weight
                heapq.heappush(pq, (key[v],v))
                parent[v] = u

    for i in range(0,len(G)):
        totalweight += key[i]
    
    return totalweight

"""
if __name__ == '__main__':
    
    filename = '../data/rmat0406.gr'
    graphfile = open(filename,'r')
    lines = graphfile.readlines()
    a = lines[0].split()

    G = nx.MultiGraph()
    G.add_nodes_from(range(0,int(a[0])))
    for i, line in enumerate(lines):
        if i == 0:
            continue
        else:
            a = line.split()
            G.add_edge(int(a[0]),int(a[1]),weight=int(a[2]))


    a = G.neighbors(0)

    computeMST(G)
"""
