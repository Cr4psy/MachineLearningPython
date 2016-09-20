#Linear kernel
import numpy as np

########
def LinearK(a, b):
    print "LinearK"
    return (np.dot(a, b) +1);
#######


def PolyK(a,b, p):
    print "PolyK"
    return ((np.dot(a,b)+1)**p);

######

def RBFK(a,b,sigma):
    print "RBF kerel"
    return


