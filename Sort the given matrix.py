def sortMatrix(mat,m,n):
    if m == 0 or n == 0:
        return "invalid matrix structure"
    
    values = []
    
    for i in range(m):
        for j in range(n):
            values.append(mat[i][j])
    
    values.sort()
    
    sortedMat = [[0]*n for i in range(m)]
    k = 0
    for i in range(m):
        for j in range(n):
            sortedMat[i][j] = values[k]
            k += 1 
    return sortedMat


m = int(input("Enter row value:"))
n = int(input("Enter column value:"))

mat = [[0]*n for i in range(m)]

for i in range(m):
    for j in range(n):
        ele = int(input("element value:"))
        mat[i][j] = ele
        
print(sortMatrix(mat,m,n))