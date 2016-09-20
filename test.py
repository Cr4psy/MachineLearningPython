#Just test program



#from kernel import LinearK
from kernel import LinearK
from kernel import PolyK
from kernel import RBFK
from kernel import SigmoidK
#Radial Basis Function kernels

import numpy as np

a= np.array([3,4,5])
b = np.array([0,0,1])
sigma = 2
k=1
delta=1

print "test"
print LinearK(a,b)
print PolyK(a,b,2)
print RBFK(a,b,sigma)
print SigmoidK(a,b,k,delta)
print "end"

