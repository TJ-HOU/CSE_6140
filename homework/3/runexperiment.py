import time, os, re
import matplotlib.pyplot as plt
from divideandconquer import *
from dynamic import *

# path where all the data is stored
path = "/Users/Alex/Dropbox/College/Fall 2017/CSE 6140/homework/3/"

# runs both findMaxSumDC and findMaxSumDP and times them
def runproblem3():

    N = []
    DC = []
    DP = []

    # reads in each file and parses data
    for f in sorted(os.listdir(path + "data/"), key=numericalSort):
        setfile = open(path + "data/" + f,'r')
        lines = setfile.readlines()
    
        n, trials = lines[0].split(',')

        setfile.close()

        # creates output files
        dcstring = "awinkles3_output_dc_" + n + ".txt"
        dpstring = "awinkles3_output_dp_" + n + ".txt"
        dcresultfile = open(path + "output/" + dcstring,'w')
        dpresultfile = open(path + "output/" + dpstring,'w')

        n = int(n)
        trials = int(trials)

        N.append(n)

        DCtime = 0.0
        DPtime = 0.0
    
        # for each trial in the file, runs DC and DP methods then writes results to file
        for i in range(1,trials+1):
            A = [float(j) for j in lines[i].split(',')]
            starttime = time.time()
            res, start, stop = findMaxSumDC(A,0,n-1)
            stoptime = (time.time() - starttime) * 1000.0
            DCtime += stoptime
            dcresultfile.write("%.2f,%d,%d,%.2f\n" % (res, start+1, stop+1, stoptime))
            
            starttime = time.time()
            res, start,stop = findMaxSumDP(A)
            stoptime = (time.time() - starttime) * 1000.0
            DPtime += stoptime
            dpresultfile.write("%.2f,%d,%d,%.2f\n" % (res, start, stop, stoptime))
            

        # closes output files when finished
        dcresultfile.close()
        dpresultfile.close()

        DCtime /= trials
        DPtime /= trials
        DC.append(DCtime)
        DP.append(DPtime)

    plt.plot(N,DC,'r',label = 'Divide and Conquer')
    plt.plot(N,DP,'b',label = 'Dynamic Programming')
    plt.ylabel('Average time (ms)')
    plt.xlabel('n')
    plt.title('Comparing Divide & Conquer and Dynamic Programming')
    plt.legend()
    plt.show()

# taken from StackOverflow to sort files properly
# https://stackoverflow.com/questions/12093940/reading-files-in-a-particular-order-in-python
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts
