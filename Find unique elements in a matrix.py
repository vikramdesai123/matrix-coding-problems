# problem statement: Find unique elements in a matrix


def uniqueMatrixElements(mat):
    row = len(mat)
    column = len(mat[0])
     
    MapVal ={}
     
    for i in range(row):
        for j in range(column):
            if mat[i][j] not in MapVal:
                MapVal[mat[i][j]] = 1
            else:
                MapVal[mat[i][j]] += 1 
    flag = False
    unique = []
    for i in MapVal:
        if MapVal[i] == 1:
            unique.append(i)
            flag = True
    if flag == False:
        return "No unique element in the matrix"
    else:
        return unique

mat = [[1,2,2],[3,5,6],[3,2,6]]
print(uniqueMatrixElements(mat))