##With slack variables

from cvxopt.solvers import qp
from cvxopt.base import matrix
from kernel import *

import numpy, pylab, random, math

C = 20
data_size = 20
threshold = 0.00001

kernel = 3 # 0 - linear
           # 1 - polynomial
           # 2 - RBFK
           # 3 - Sigmoid

def kernelFunction(kernel_num, xi, yi, xj, yj, var=0):
    x_array = numpy.array([xi, yi])
    y_array = numpy.array([xj, yj])
    if kernel_num == 0:
        return LinearK(x_array, y_array)
    elif kernel_num == 1:
        return PolyK(x_array, y_array, var)
    elif kernel_num == 2:
        return RBFK(x_array, y_array, var)
    else:
        return SigmoidK(x_array, y_array,k=var)


def non_zero_alpha_values(alpha, data):
    non_zero_elements = []
    for i in range(len(alpha)):
        if not alpha[i] < threshold: 
            non_zero_elements.append((alpha[i], data[i]))
    return non_zero_elements


def create_p_matrix(data, kernel_num, var):
    P = [[0 for x in range(data_size)] for y in range(data_size)]
    for i in range(data_size):
        for j in range(data_size):
            xi, yi, li = data[i]
            xj, yj, lj = data[j]
            P[i][j] = li * lj * kernelFunction(kernel_num, xi, yi, xj, yj,var)
    return P   

def create_g_matrix():
    G0 = numpy.zeros((2*data_size,data_size))
    i = 0
    j = 0
    while i<(data_size):
        G0[i][i]= -1
        i+=1
    while i < data_size * 2:
        G0[i][j]=1
        i+=1
        j+=1
    return G0

def indicator(x_new, alpha,kernel_num, var):
    index = 0
    for i in range(len(alpha)):
        ai, tuple = alpha[i]
        index = index + ai * tuple[2] * kernelFunction(kernel_num, x_new[0],
                                                       x_new[1], tuple[0], tuple[1], var)
    return index                   
	
    
def main():
    # Generate test data
    classA = [(random.normalvariate(-1.5,1),random.normalvariate(0.5,1),1.0) \
    for i in range(data_size / 4)] + [(random.normalvariate(1.5,1), \
    random.normalvariate(0.5,1),1.0) for i in range(data_size / 4)]

    classB = [(random.normalvariate(0,0.5),random.normalvariate(-0.5,0.5), \
    -1.0) for i in range(data_size / 2)]

    data = classA + classB
    random.shuffle(data)


    for i in range(1,2):
        kernel=3
        var=1
        # Create necessary matrixes and vectors
        P = create_p_matrix(data, kernel,var)
        G = create_g_matrix()
        q = numpy.zeros((data_size, 1))
        q.fill(-1)
        h = numpy.zeros((data_size, 1))
        h.fill(C)
        h = numpy.concatenate((numpy.zeros((data_size,1)),h))
        r = qp(matrix(P), matrix(q), matrix(G), matrix(h))        
        alpha = list(r['x'])
        alpha_without_zeros = non_zero_alpha_values(alpha, data)
        print alpha_without_zeros
        new_point = [3, 0]
        classified = indicator(new_point, alpha_without_zeros, kernel,var)
        print "Classified: {}".format(classified)
        xrange = numpy.arange(-4, 6, 0.05)
        yrange = numpy.arange(-4, 6, 0.05)
        grid = matrix([[indicator((x, y), alpha_without_zeros,kernel,var) for y in yrange] \
           for x in xrange])
        pylab.hold(True)
        pylab.contour(xrange, yrange, grid,
                  (-1.0, 0.0, 1.0),
                  colors=('red', 'black', 'blue'),
                  linewidths=(1, 3, 1))
        pylab.plot([p[0] for p in classA],[p[1] for p in classA],'bo')
        pylab.plot([p[0] for p in classB],[p[1] for p in classB], 'ro')
        pylab.plot(new_point[0], new_point[1], 'go')
        pylab.show()








if __name__ == '__main__':
   main()

