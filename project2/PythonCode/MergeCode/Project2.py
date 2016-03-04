from GenerateA import *
from SolveTheta import *
from CalculateB import *
import numpy as np
from CalculateEigV import *
import matplotlib.pyplot as plt
import numpy.linalg as la

n = 4
rho_max = 1
err = 1E-8
A = construct_A(n, rho_max)
# print(A)
w, v = la.eig(A)
print "w = ",w
print "v = ",v
maxValue = 999
EigV = np.diag(np.ones(5))
maxReturn = A_max(A)
maxValue = maxReturn[2]
maxPosition = maxReturn[0:2]

while np.abs(maxValue) > err:

    theta = solveTheta(A, maxPosition[0], maxPosition[1])
    B = CalculateB(A, theta, maxPosition[0], maxPosition[1])
    EigV = CalculateEigV(EigV, theta, maxPosition[0], maxPosition[1])
    # print 'EigV = ', EigV
    A = B
    maxReturn = A_max(A)
    maxValue = maxReturn[2]
    maxPosition = maxReturn[0:2]

print "B = ",B
print "Eig vectors = ", EigV

Bdiag = np.diag(B)
plt.plot(EigV)
# plt.show()

Bdiag = np.diag(B)
E = Bdiag*EigV

# print EigV
