import math
import numpy
from numpy import *
import numpy as np
from scipy.special import comb, perm

rho=array([[1,2,3,4,9,10,11,12,3,8],[1,2,3,4,9,10,11,12,3,1],[1,2,3,4,9,10,11,12,3,8],[1,2,3,4,9,10,11,12,3,1],[1,2,3,4,9,10,11,12,3,8],[1,2,3,4,9,10,11,12,3,1],[1,2,3,4,9,10,11,12,3,8],[1,2,3,4,9,10,11,12,3,1],[1,2,3,4,9,10,11,12,3,8],[1,2,3,4,9,10,11,12,3,1]])

N=10
Ɵ=5
Ψ=5

sum=0

for i in range(0, N+1, 1):
    for j in range(0, N+1, 1):  
        sum+=((comb(N,i)*comb(N,j))**0.5)*(math.cos(Ɵ/2)**(i+j))*(math.sin(Ɵ/2)**(2*N-i-j))*(math.e**(1j*Ψ*(j-i)))*rho[i-1,j-1]
print(sum)

