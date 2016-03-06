import numpy as np
from copy import copy

def construct_A2(n, rho_max, wr):

    # define A, h (step), rho[i], and rho_min
    rho_min = 0
    rho = np.ones(n)
    h = (rho_max - rho_min)/np.double(n)
    V = np.ones(n)
    d = np.ones(n)
    e = -np.ones(n-1)*1/np.square(h)

    # constructing_A
    for i in range(n):         # to create rho_i (from i = 0 to n-1
        rho[i] = rho_min + (i+1)*h
        V[i] = np.square(rho[i])*wr*wr+1.0/rho[i]
        d[i] = 2/np.square(h) + V[i]

    A = np.identity(n)*d + np.diag(e, -1) + np.diag(e, 1)
    A_max = A[n-1, n-1]
    EigV = np.ones(n)

    return A


def main():
    print construct_A2(5,1,0.1)

if __name__ == "__main__":
    main()