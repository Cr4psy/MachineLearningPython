#from kernel import LinearK
from kernel import LinearK
from kernel import PolyK

import numpy as np

a= np.array([1,2,3])

b = np.array([0,0,1])


print "test"
print LinearK(a,b)
print PolyK(a,b,2)

print "end"
