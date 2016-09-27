from cvxopt.solvers import qp
from cvxopt.base import matrix
from kernel import LinearK

import numpy, pylab, random, math


def non_zero_alpha_values(matrix):
    return []

# Build matrix P from a given set of data points
P = [1, 2, 3]

C = matrix(P)

classA = [(random.normalvariate(-1.5,1),random.normalvariate(0.5,1),1.0) for i in range(5)] + \
   [(random.normalvariate(1.5,1),random.normalvariate(0.5,1),1.0) for i in range(5)]

classB = [(random.normalvariate(0,0.5),random.normalvariate(-0.5,0.5),-1.0) for i in range(10)]

data = classA + classB

random.shuffle(data)
print len(data)


pylab.hold(True)
pylab.plot([p[0] for p in classA],[p[1] for p in classA],'bo')
pylab.plot([p[0] for p in classB],[p[1] for p in classB], 'ro')
pylab.show()

# Build the q vector, G matrix and h vector
# SIZE IS TEMPORARY
q = [-1] * 100
h = [0] * 100

print LinearK(1,2)
