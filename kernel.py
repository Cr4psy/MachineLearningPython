##Contains all kernels

#Linear kernel
import numpy as np
import math

########
def LinearK(a, b):
    return (np.dot(a, b) + 1);
#######


def PolyK(a, b, p):
    print "PolyK"
    return ((np.dot(a, b) + 1) ** p);

######

def RBFK(a, b, sigma):
    print "RBF kernel"
    return math.exp(-(np.linalg.norm( a - b)) ** 2 / (2 * sigma ** 2))

######

def SigmoidK(a, b, k, delta):
    print "Sigmoid kernel"
    return np.tanh(np.dot(k * a, b) - delta)
