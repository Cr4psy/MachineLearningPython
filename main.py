from cvxopt.solvers import qp
from cvxopt.base import matrix
from kernel import *

import numpy, pylab, random, math

data_size = 20

def non_zero_alpha_values(alpha):
    non_zero_elements = []
    for element in alpha:
        return 0
 
def create_p_matrix(data):
    P = [[0 for x in range(data_size)] for y in range(data_size)]
    for i in range(data_size):
        for j in range(data_size):
            xi, yi, li = data[i]
            xj, yj, lj = data[j]
            P[i][j] = li * lj * LinearK([xi, yi], [xj, yj])
    return P   

def create_g_matrix():
    G = numpy.zeros((data_size, data_size))
    numpy.fill_diagonal(G, -1)
    return G

def main():
    classA = [(random.normalvariate(-1.5,1),random.normalvariate(0.5,1),1.0) \
    for i in range(data_size / 4)] + [(random.normalvariate(1.5,1), \
    random.normalvariate(0.5,1),1.0) for i in range(data_size / 4)]

    classB = [(random.normalvariate(0,0.5),random.normalvariate(-0.5,0.5), \
    -1.0) for i in range(data_size / 2)]

    data = classA + classB
    random.shuffle(data)
    P = create_p_matrix(data)
    G = create_g_matrix()
    q = numpy.zeros((data_size, 1))
    q.fill(-1)
    h = numpy.zeros((data_size, 1))
    r = qp(matrix(P), matrix(q), matrix(G), matrix(h))
    alpha = list(r['x'])
    print alpha
    
#pylab.hold(True)
#pylab.plot([p[0] for p in classA],[p[1] for p in classA],'bo')
#pylab.plot([p[0] for p in classB],[p[1] for p in classB], 'ro')
#pylab.show()


if __name__ == '__main__':
   main()

