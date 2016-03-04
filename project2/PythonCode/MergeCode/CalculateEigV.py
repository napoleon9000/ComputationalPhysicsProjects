import numpy as np
from copy import copy


# from SolveTheta import *

def CalculateEigV(EigV, theta, p, q):
    sizeEigV = np.sqrt(EigV.size)
    S = np.diag(np.ones(sizeEigV))
    s = theta[0]
    c = theta[1]
    S[p, p] = c
    S[p, q] = -s
    S[q, p] = s
    S[q, q] = c
    EigV = S*EigV
    #for i in range(0, int(sizeEigV)):
        # print "Out i, p, q", i, p, q
        # print (i != p) & ( i != q)
        #if (i != p) & (i != q):
            # print 'i, p, q = ', i, p, q
            #EigVp = EigV[i, p]
            # print 'EigVp = ',EigVp
            #EigVq = EigV[i, q]
            # print "EigVq = ",EigVq
            #EigV[i, p] = s * EigVp - c * EigVq
            #EigV[i, q] = s * EigVp + c * EigVq
            # print "EigV = ",EigV
    return EigV


def main():
    print CalculateEigV(np.ones([5, 5]), [0.707, 0.707], 2, 3)


if __name__ == '__main__':
    main()
