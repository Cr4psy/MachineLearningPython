##Contains all kernels

#Linear kernel
import numpy as np
import math

########
def LinearK(a, b):
    result = (np.dot(a, b) + 1)
    return result;
#######


def PolyK(a, b, p=4):
    return ((np.dot(a, b) + 1) ** p);

######

def RBFK(a, b, sigma=1):
    return math.exp(-(np.linalg.norm((a - b))) ** 2 / (2 * sigma ** 2))

######

def SigmoidK(a, b, k=1, delta=0.2):
    return np.tanh(np.dot((k * a), b) - delta)
