# problem statement:  addition of two matrice

# Given two N x M matrices. 
# Find a N x M matrix as the sum of given matrices each value at the 
# sum of values of corresponding elements of the given two matrices.


def matrixAddition(matrix1,matrix2):
    resultMatrix = [[0]*2 for i in range(2)]
    
    l = len(matrix1)
    for i in range(l):
        for j in range(l):
            resultMatrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return resultMatrix

matrix1 = [[1,2],[3,4]]
matrix2 = [[4,5],[6,7]]

print(matrixAddition(matrix1,matrix2))