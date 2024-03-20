import unittest
import numpy as np
from faktoryzacja import make_U_and_L
import copy as cp

class TestFactor(unittest.TestCase):

    def test_0(self):
        A = [[5,3,2],[1,2,0],[3,0,4]]

        A = make_U_and_L(A)

        U = [[0 for _ in range(len(A))] for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(i,len(A)):
                U[i][j] = A[i][j]

        np_U = np.array(U)

        L = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(0,i+1):
                if i == j:
                    L[i][j] = 1
                else:
                    L[i][j] = A[i][j]
            
        np_L = np.array(L)

        A_np = np.dot(np_L,np_U)

        A = [[5,3,2],[1,2,0],[3,0,4]]

        B = [[abs(A[i][j]-A_np[i][j]) for j in range(len(A))]for i in range(len(A))]

        for i in range(len(B)):
            for j in range(len(B)):
                self.assertAlmostEqual(B[i][j],0)
            

    def test_1(self):
        A = [[0 for _ in range(100)] for _ in range(100)]
        for i in range(100):
            for j in range(100):
                A[i][j] = np.random.randint(0,100)

        A_t = cp.deepcopy(A)
        A = make_U_and_L(A)

        U = [[0 for _ in range(len(A))] for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(i,len(A)):
                U[i][j] = A[i][j]

        np_U = np.array(U)

        L = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(0,i+1):
                if i == j:
                    L[i][j] = 1
                else:
                    L[i][j] = A[i][j]
            

        np_L = np.array(L)

        A_np = np.dot(np_L,np_U)

        A = [[5,3,2],[1,2,0],[3,0,4]]

        B = [[abs(A_t[i][j]-A_np[i][j]) for j in range(len(A))]for i in range(len(A))]

        for i in range(len(B)):
            for j in range(len(B)):
                self.assertAlmostEqual(B[i][j],0)


    def test_2(self):
        A = [[0 for _ in range(100)] for _ in range(100)]
        for i in range(100):
            for j in range(100):
                A[i][j] = np.random.randint(0,100)

        A_t = cp.deepcopy(A)
        A = make_U_and_L(A)

        U = [[0 for _ in range(len(A))] for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(i,len(A)):
                U[i][j] = A[i][j]

        np_U = np.array(U)

        L = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(0,i+1):
                if i == j:
                    L[i][j] = 1
                else:
                    L[i][j] = A[i][j]
            

        np_L = np.array(L)

        A_np = np.dot(np_L,np_U)

        A = [[5,3,2],[1,2,0],[3,0,4]]

        B = [[abs(A_t[i][j]-A_np[i][j]) for j in range(len(A))]for i in range(len(A))]

        for i in range(len(B)):
            for j in range(len(B)):
                self.assertAlmostEqual(B[i][j],0)


    def test_3(self):
        A = [[0 for _ in range(100)] for _ in range(100)]
        for i in range(100):
            for j in range(100):
                A[i][j] = np.random.randint(0,100)

        A_t = cp.deepcopy(A)
        A = make_U_and_L(A)

        U = [[0 for _ in range(len(A))] for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(i,len(A)):
                U[i][j] = A[i][j]

        np_U = np.array(U)

        L = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(0,i+1):
                if i == j:
                    L[i][j] = 1
                else:
                    L[i][j] = A[i][j]
            

        np_L = np.array(L)

        A_np = np.dot(np_L,np_U)

        A = [[5,3,2],[1,2,0],[3,0,4]]

        B = [[abs(A_t[i][j]-A_np[i][j]) for j in range(len(A))]for i in range(len(A))]

        for i in range(len(B)):
            for j in range(len(B)):
                self.assertAlmostEqual(B[i][j],0)


    def test_4(self):
        A = [[0 for _ in range(100)] for _ in range(100)]
        for i in range(100):
            for j in range(100):
                A[i][j] = np.random.randint(0,100)

        A_t = cp.deepcopy(A)
        A = make_U_and_L(A)

        U = [[0 for _ in range(len(A))] for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(i,len(A)):
                U[i][j] = A[i][j]

        np_U = np.array(U)

        L = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(0,i+1):
                if i == j:
                    L[i][j] = 1
                else:
                    L[i][j] = A[i][j]
            

        np_L = np.array(L)

        A_np = np.dot(np_L,np_U)

        A = [[5,3,2],[1,2,0],[3,0,4]]

        B = [[abs(A_t[i][j]-A_np[i][j]) for j in range(len(A))]for i in range(len(A))]

        for i in range(len(B)):
            for j in range(len(B)):
                self.assertAlmostEqual(B[i][j],0)


    def test_5(self):
        A = [[0 for _ in range(100)] for _ in range(100)]
        for i in range(100):
            for j in range(100):
                A[i][j] = np.random.randint(0,100)

        A_t = cp.deepcopy(A)
        A = make_U_and_L(A)

        U = [[0 for _ in range(len(A))] for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(i,len(A)):
                U[i][j] = A[i][j]

        np_U = np.array(U)

        L = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(0,i+1):
                if i == j:
                    L[i][j] = 1
                else:
                    L[i][j] = A[i][j]
            

        np_L = np.array(L)

        A_np = np.dot(np_L,np_U)

        A = [[5,3,2],[1,2,0],[3,0,4]]

        B = [[abs(A_t[i][j]-A_np[i][j]) for j in range(len(A))]for i in range(len(A))]

        for i in range(len(B)):
            for j in range(len(B)):
                self.assertAlmostEqual(B[i][j],0)



if __name__ == '__main__':
    unittest.main()
