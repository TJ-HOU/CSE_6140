#!/usr/bin/python
##  CSE6140 HW1
##  This assignment requires installation of networkx package if you want to make use of available graph data structures or you can write your own!!
##  Please feel free to modify this code or write your own
import networkx as nx
import time
import sys
from computeMST import computeMST

class RunExperiments:
    def read_graph(self, filename):
        #make sure to add to filename the directory where it is located and the extension .txt
        #G = nx.MultiGraph()
        #if you want to use networkx

        #Write code to add nodes and edges
        #Check out add_node, add_edge in networkx

        graphfile = open(filename,'r')
        lines = graphfile.readlines()
        a = lines[0].split()
        MG = nx.MultiGraph()
        MG.add_nodes_from(range(0,int(a[0])))

        for i, line in enumerate(lines):
            if i != 0:
                a = line.split()
                MG.add_edge(int(a[0]),int(a[1]),weight=int(a[2]))

        G = nx.Graph()
        G.add_nodes_from(range(0,int(a[0])))
        for u in range(0,len(MG)):
            for v in MG[u]:
                val = sys.maxint
                if v > u:
                    for j in MG[u][v]:
                        if (MG[u][v][j]['weight'] < val):
                            val = MG[u][v][j]['weight']
                    G.add_edge(u,v,weight=val)

        return G

    def main(self):

        num_args = len(sys.argv)

        if num_args < 4:
            print "error: not enough input arguments"
            exit(1)

        graph_file = sys.argv[1]
        change_file = sys.argv[2]
        output_file = sys.argv[3]

        #Construct graph
        G = self.read_graph(graph_file)

        start_MST = time.time() #time in seconds
        MSTweight = computeMST(G) #call MST function to return total weight of MST
        total_time = (time.time() - start_MST) * 1000 #to convert to milliseconds

        #Write initial MST weight and time to file
        output = open(output_file, 'w')
        output.write(str(MSTweight) + " " + str(total_time) + "\n")


        #Changes file
        with open(change_file, 'r') as changes:
            num_changes = changes.readline()

            for line in changes:
                #parse edge and weight
                edge_data = list(map(lambda x: int(x), line.split()))
                assert(len(edge_data) == 3)

                u,v,val = edge_data[0], edge_data[1], edge_data[2]

                try:
                    if G[u][v]['weight'] > val:
                        G[u][v]['weight'] = val
                except:        
                    G.add_edge(u,v,weight=val)

                #call recomputeMST function
                start_recompute = time.time()
                new_weight = computeMST(G)
                total_recompute = (time.time() - start_recompute) * 1000 # to convert to milliseconds

                #write new weight and time to output file
                output.write(str(new_weight) + " " + str(total_recompute) + "\n")



if __name__ == '__main__':
    # run the experiments
    runexp = RunExperiments()
    runexp.main()
