from GenerateA import *
from SolveTheta import *
from CalculateB import *
import numpy as np
from CalculateEigV import *
import matplotlib.pyplot as plt
import numpy.linalg as la
from GenerateA2 import *
from GenerateA2w import *
import time

def argsort(seq):
    return [x for x,y in sorted(enumerate(seq), key = lambda x: x[1])]

n = 100
rho_max = 5
err = 1E6
wr = 1
system = 1
for wr in [0.01, 0.5, 1, 5]:
    if system == 0:
        A = construct_A(n, rho_max)
    if system == 1:
        A = construct_A2(n, rho_max, wr)
    if system == 2:
         A = construct_A2w(n, rho_max, wr)
    # print(A)
    w, v = la.eig(A)
    # print "w = ",w
    # print "v = ",v
    maxValue = 999
    EigV = np.diag(np.ones(n))
    maxReturn = A_max(A)
    maxValue = maxReturn[2]
    maxPosition = maxReturn[0:2]
    start = time.clock()                   # Start counting time
    while np.abs(maxValue) > err:
        theta = solveTheta(A, maxPosition[0], maxPosition[1])
        B = CalculateB(A, theta, maxPosition[0], maxPosition[1])
        EigV = CalculateEigV(EigV, theta, maxPosition[0], maxPosition[1])
        A = B
        maxReturn = A_max(A)
        maxValue = maxReturn[2]
        maxPosition = maxReturn[0:2]

    finish = time.clock()
    oriEigValue = np.diag(A)
    oriEigValue = w
    sortIdx = argsort(oriEigValue)
    EigenValues = sorted(np.diag(A))

    print "Three lowest Eigen values = ", EigenValues[0:3]
    print "The time used for calculation is ", finish-start

    alpha = (6.63E-34)*(6.63E-34)/(9.1E-31*9E9*1.6E-19*1.6E-19)*1E10 # in Angstrom
    rmax = rho_max*alpha
    r = np.arange(n)/float(n)
    r = (r + r[1])*rmax
    stepLength = rmax/n
    # print r
    EigV = v
    Bdiag = np.diag(A)
    EigV1 = EigV[:,sortIdx[0]]*EigV[:,sortIdx[0]]
    EigV2 = EigV[:,sortIdx[1]]*EigV[:,sortIdx[1]]
    EigV3 = EigV[:,sortIdx[2]]*EigV[:,sortIdx[2]]
    EigV1 = EigV1/sum(stepLength*EigV1)
    # print sum(stepLength*EigV1)
    # print la.norm(EigV1)
    EigV2 = EigV2/sum(stepLength*EigV2)
    EigV3 = EigV3/sum(stepLength*EigV3)
    plt.plot(r,EigV1, label='E0,rho = '+ str(rho_max) + ',wr = ' + str(wr) + ',system = '+ str(system))
    #plt.plot(r,EigV2, label='E1,rho = '+ str(rho_max) + ',wr = ' + str(wr) + ',system = '+ str(system))
    #plt.plot(r,EigV3, label='E2,rho = '+ str(rho_max) + ',wr = ' + str(wr) + ',system = '+ str(system))
plt.legend(loc = 1)
plt.xlabel('r/A')
plt.ylabel('Probability')
plt.show()

# print EigV
