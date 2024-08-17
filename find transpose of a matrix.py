def transposeMatrix(mat,m,n):
    
    values = []
    
    for i in range(n):
        for j in range(m):
            val = mat[j][i]
            values.append(val)
    
    transMat = [[0]*m for i in range(n)]
    k = 0
    for i in range(n):
        for j in range(m):
            transMat[i][j] = values[k]
            k += 1 
    return transMat


m = int(input("Enter row value:"))
n = int(input("Enter column value:"))

mat = [[0]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        ele = int(input("enter matrix elements:"))
        mat[i][j] = ele
print("original matrix:",mat)
print("Matrix after transpose:",transposeMatrix(mat,m,n))