
#!/bin/python3

import math
import os
import random
import re
import sys
import operator

# Complete the boardCutting function below.
def boardCutting(cost_y, cost_x):
    totalcost=0
    ylist=0
    xlist=0
    cost_y.update(cost_x)
    dxs=dict(sorted(cost_y.items(), key=operator.itemgetter(1),reverse=True))
    for l,m in dxs.items():
        if(l<o-1):
            totalcost+=(xlist+1)*m
            ylist+=1
        else:
            totalcost+=(ylist+1)*m
            xlist+=1
    return totalcost%((10**9)+7)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        y=0
        x=0
        cost_y={}
        cost_x={}
        op = input().split()

        o = int(op[0])

        p = int(op[1])
        for i in input().rstrip().split():
            cost_y[y]=int(i)
            y+=1
        for i in input().rstrip().split():
            cost_x[y]=int(i)
            y+=1
        result = boardCutting(cost_y, cost_x)

        fptr.write(str(result) + '\n')

    fptr.close()
