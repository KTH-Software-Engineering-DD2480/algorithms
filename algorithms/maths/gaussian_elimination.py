"""
Implementation of gaussian elimination for numpy array inputs

Example System 1:
x + x_2 = 1
2x + x_2 = 1


Input: 
coeff = [[1,1],[2,1]]
y = [1,1]

Output:
[0.0, 1.0]
"""

def gaussianElimination(coeff, y):
    """Gaussian elimination with back substitution"""
    n = len(y)
    
    for i in range(n-1):
        for j in range(i+1, n):
            if(coeff[i][i]==0):
                print("DIVIDED BY 0")
            # divide by the upper row
            m = coeff[j][i]/coeff[i][i]
            for x in range(i, n):
                # update the row
                coeff[j][x] = coeff[j][x] - m*coeff[i][x]
            # update y's
            y[j] = y[j] - m*y[i]
    print("The solution is")
    print(backSubsitution(coeff, y, n))

def backSubsitution(coeff, y, n):
    """Back substitution to get the solutions"""
    # array for the solution
    sol = [0]*n
    print("it is ", coeff[n-1][n-1])
    sol[n-1] = y[n-1]/coeff[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = y[i]
        for j in range(i+1, n):
            sum = sum - coeff[i][j]*sol[j]
        sol[i] = sum/coeff[i][i]
    return sol

    
    

    
    