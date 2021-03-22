import os
import matplotlib.pyplot as plt

path = "/Users/Alex/Dropbox/College/Fall 2017/CSE 6140/homework/1/MST/"

def analyze_MST(path):
    edges = []
    static_time = []
    dynamic_time = []

    for f in os.listdir(path + "data/"):
        if f.endswith(".gr"):
            gfile = open(path + "data/" + f,'r')
            lines = gfile.readlines()
            a = lines[0].split()
            edges.append(int(a[1]))
   
    for f in os.listdir(path + "results/"):
        if f.endswith(".out"):
            sumval = 0
            output = open(path + "results/" + f,'r')
            lines = output.readlines()
            for i, line in enumerate(lines):
                a = line.split()
                if i ==0: 
                    static_time.append(float(a[1]))
                else:
                    sumval += float(a[1])
            dynamic_time.append(sumval)


    plt.plot(edges,static_time,'bo-',label='Static')
    plt.title('MST Computation with Prim\'s Algorithm - Static')
    plt.ylabel('Time (ms)')
    plt.xlabel('Edges')
    plt.show()
                 
    plt.plot(edges,dynamic_time,'ro-',label='Dynamic')
    plt.title('MST Computation with Prim\'s Algorithm - Dynamic')
    plt.ylabel('Time (ms)')
    plt.xlabel('Edges')
    plt.show()

analyze_MST(path)
