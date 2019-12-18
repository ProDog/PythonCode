from multiprocessing import Pool
from itertools import product
import time

def calSquare(x,y):
    return x*y+y*8*x

global arr   

a1=[2,4,6,7,8,10,-5,0,26]
b1=[4,4,4,4,4,4,-4,4,4]

time_start=time.time()
if __name__=='__main__':
    with Pool(5) as p:
        print(p.starmap(calSquare,zip(a1,b1)))        
        time_end=time.time()
        print(time_end-time_start)

    time_start=time.time()
    for i in range(0,9,1):
        print(calSquare(a1[i],b1[i]),end=' ')
    time_end=time.time()
    print(time_end-time_start)