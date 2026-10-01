import numpy as np

def cholesky(A):
    # test for symmetry
    # print(np.allclose(A,A.T))


    # Test for positive definiteness

    # A symmetric matrix is positive definite if all of its eigenvalues are positive. so let's get the eigenvalues

    eigenvalues = np.linalg.eigvalsh(A)
    # print(eigenvalues)

    num = A.shape[0]
    L = np.zeros_like(A)

    for i in range(num):
            for j in range(i+1):
                if i==j:
                    L[i,j] =  np.sqrt(A[i,i] - np.sum(L[i,:j]**2)) 
                    
                    
                else:
                    L[i,j] = (A[i, j] - np.dot(L[i, :j], L[j, :j])) / L[j,j]

    return L