from cvxopt.solvers import qp
from cvxopt.base import matrix
from kernel import LinearK

import numpy, pylab, random, math


P = [1,2,3]

C = matrix(P)

classA = [(random.normalvariate(-1.5,1),random.normalvariate(0.5,1),1.0) for i in range(5)] + \
   [(random.normalvariate(1.5,1),random.normalvariate(0.5,1),1.0) for i in range(5)]

classB =  [(random.normalvariate(0,0.5),random.normalvariate(-0.5,0.5),-1.0) for i in range(10)]

data = classA + classB

random.shuffle(data)


pylab.hold(True)
pylab.plot([p[0] for p in classA],[p[1] for p in classA],'bo')
pylab.plot([p[0] for p in classB],[p[1] for p in classB], 'ro')
pylab.show()

LinearK(1,2)
