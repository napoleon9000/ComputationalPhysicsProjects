import unittest
from GenerateA import *
from SolveTheta import *
from CalculateB import *
from CalculateEigV import *
from GenerateA2 import *
from GenerateA2w import *
import numpy as np
import numpy.linalg as la


class TestStringMethods(unittest.TestCase):
    def test_GenerateA(self):
        err = 1E-6
        A3 = np.array([[18, -9, 0], [-9, 18.111111, -9, ], [0, -9, 18.444444]])
        A4 = np.array([[32, -16, 0, 0], [-16, 32.0625, -16, 0], [0, -16, 32.25, -16], [0., 0, -16, 32.5625]])
        self.assertTrue(la.norm(construct_A(3, 1)) - la.norm(A3) < err)
        self.assertTrue(la.norm(construct_A(4, 1)) - la.norm(A4) < err)

    def test_maxA(self):
        A_diag = np.diag([1, 1, 1])
        A_negative = np.diag([1, 1, 1])+0.1
        A_negative[1,2] = -2
        max_A_diag = A_max(A_diag)
        max_A_negative = A_max(A_negative)
        self.assertEqual(max_A_diag[2], 0)
        self.assertEqual(max_A_negative[0], 1)
        self.assertEqual(max_A_negative[1], 2)
        self.assertEqual(max_A_negative[2], -2)

    def test_SolveThera(self):
        err = 1E-6
        A = np.matrix('1 2 0; 2 1 2; 0 2 1')
        p = 1
        q = 2
        theta = solveTheta(A, p, q)
        self.assertTrue(theta[0]-np.sqrt(2)/2.0 <err)
        self.assertTrue(theta[1]-np.sqrt(2)/2.0 <err)

    def test_CalculateB(self):
        A = np.matrix('1.0 2 3; 2 1 2; 3 2 1')
        p = 0
        q = 2
        theta = solveTheta(A, p, q)
        B = CalculateB(A, theta, p, q)
        self.assertTrue(B[p,q] == 0)



if __name__ == '__main__':
    unittest.main()
