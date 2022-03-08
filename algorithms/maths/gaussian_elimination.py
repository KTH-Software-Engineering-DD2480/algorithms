"""
Implementation of gaussian elimination for numpy array inputs partial pivoting, to avoid division by zero

Example System 1:
x + x_2 = 1
2x + x_2 = 1


Input: 
coeff = [[1,1],[2,1]]
y = [1,1]

Output:
[0.0, 1.0]
"""
import numpy as np

# def gaussianElimination(coeff, y):
#     """Gaussian elimination with back substitution"""
#     n = len(y)
    
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if(coeff[i][i]==0):
#                 print("DIVIDED BY 0")
#             # divide by the upper row
#             m = coeff[j][i]/coeff[i][i]
#             for x in range(i, n):
#                 # update the row
#                 coeff[j][x] = coeff[j][x] - m*coeff[i][x]
#             # update y's
#             y[j] = y[j] - m*y[i]
#     #print("The solution is")
#     print(backSubsitution(coeff, y, n))
#     print(coeff)
#     print(y)
#     return backSubsitution(coeff, y, n)


    
def gaussianElimination(A, b):
    """Gaussian elimination with back substitution with pivoting"""
    n = len(b)
    m = len(A)
    h = 0
    k = 0
    
    while h < m and k < n:
        temp = [abs(A[i][k]) for i in range(h,m)]
        i_max = temp.index(max(temp))
        if(A[i_max][k] == 0):
            k = k + 1
        else:
            A[h], A[i_max] = A[i_max], A[h]
            b[h], b[i_max] = b[i_max], b[h]
            for i in range(h+1, m):
                f = A[i][k]/A[h][k]
                A[i][k]=0
                for j in range(k+1, n):
                    A[i][j] = A[i][j] - A[h][j]*f
                b[i] = b[i] - f*b[i]
            h = h+1
            k = k+1
    #print("The solution is")
    print(A)
    print(b)
    print(backSubsitution(A, b, n))
    #return backSubsitution(coeff, y, n)

def backSubsitution(A, b, n):
    """Back substitution to get the solutions"""
    # array for the solution
    sol = [0]*n
    #print("it is ", coeff[n-1][n-1])
 
    sol[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum = sum + A[i][j]*sol[j]
        if(A[i][i] == 0):
            sol[i] = 0
        else:
            sol[i] = (b[i] - sum)/A[i][i]
    return sol

# def backSubsitution(coeff, y, n):
#     """Back substitution to get the solutions"""
#     # array for the solution
#     sol = [0]*n
#     #print("it is ", coeff[n-1][n-1])
#     sol[n-1] = y[n-1]/coeff[n-1][n-1]
#     for i in range(n-2, -1, -1):
#         sum = y[i]
#         for j in range(i+1, n):
#             sum = sum - coeff[i][j]*sol[j]
#         sol[i] = sum/coeff[i][i]
#     return sol

#a = np.array([[1,1,-1], [6,2,2], [-3,4,1]])
#a =  np.array([[2, 1,-1], [-3,-1,2], [-2,1,2]]) 
#b = np.array([8, -11, -3])
#answ:2 3 -1
#a=[[1,1,-1], [6,2,2], [-3,4,1]]
#b=[-3,2,1]
#b = np.array([-3,2,1])
a=[[1,1],[2,1]]
b=[1,1]
#a = [[2,-3,5],[1,2,-1],[6,-1,0]]
#b = [10, 18, 12]
gaussianElimination(a, b)
    

    
    