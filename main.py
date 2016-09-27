from cvxopt.solvers import qp
from cvxopt.base import matrix
from kernel import *

import numpy, pylab, random, math

data_size = 52
threshold = 0.00001

def non_zero_alpha_values(alpha, data):
    non_zero_elements = []
    for i in range(len(alpha)):
        if not alpha[i] < threshold: 
            non_zero_elements.append((alpha[i], data[i]))
    return non_zero_elements


def create_p_matrix(data):
    P = [[0 for x in range(data_size)] for y in range(data_size)]
    for i in range(data_size):
        for j in range(data_size):
            xi, yi, li = data[i]
            xj, yj, lj = data[j]
            P[i][j] = li * lj * PolyK([xi, yi], [xj, yj])
    return P   

def create_g_matrix():
    G = numpy.zeros((data_size, data_size))
    numpy.fill_diagonal(G, -1)
    return G

def indicator(x_new, alpha):
    index = 0
    for i in range(len(alpha)):
        ai, tuple = alpha[i]
        index = index + ai * tuple[2] * PolyK(x_new, [tuple[0], tuple[1]])
    return index                   
	
    
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
    print q
    alpha = list(r['x'])

    alpha_without_zeros = non_zero_alpha_values(alpha, data)
    print alpha_without_zeros
    new_point = [4, -3]
    classified = indicator(new_point, alpha_without_zeros)
    print "Classified: {}".format(classified)
    xrange = numpy.arange(-4, 4, 0.05)
    yrange = numpy.arange(-4, 4, 0.05)
    grid = matrix([[indicator((x, y), alpha_without_zeros) for y in yrange] \
           for x in xrange])
    pylab.hold(True)
    pylab.plot([p[0] for p in classA],[p[1] for p in classA],'bo')
    pylab.plot([p[0] for p in classB],[p[1] for p in classB], 'ro')
    pylab.plot(new_point[0], new_point[1], 'go')
    pylab.contour(xrange, yrange, grid,
                  (-1.0, 0.0, 1.0),
                  colors=('red', 'black', 'blue'),
                  linewidths=(1, 3, 1))
    pylab.show()


if __name__ == '__main__':
   main()

