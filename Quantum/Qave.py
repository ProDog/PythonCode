import math
import numpy
from numpy import *
import numpy as np
from scipy.special import comb, perm

Ɵ=math.pi/2
Ψ=0
m=10

def Qace(m,Ɵ,Ψ):
    result = 0
    for n in range(0,m+1,1):
        Qmn = 0
        for k1 in range(0,n+1,1):
            for k2 in range(0,n+1,1):
                Qmn += (math.cos(k1*Ɵ/2))*(math.sin(Ψ/2)**(n-k1))*(math.cos(k2*Ɵ/2))*(math.sin(Ψ/2)**(n-k2))
        Qmn = (n+1)*Qmn/(4*math.pi)
        result += Qmn
    return result

print(Qace(m,Ɵ,Ψ))
