# problem statement: Find distinct elements common to all rows of a matrix


def dictinctElement(mat):
    row = len(mat)
    column = len(mat[0])
    
    elementMap = {}
    for i in range(column):
        elementMap[mat[0][i]]=0
      
    for i in range(row):
        for j in range(column):
            if (mat[i][j] in elementMap) and (elementMap[mat[i][j]] == i):
                elementMap[mat[i][j]] = i + 1 
                
                if i == row-1:
                    print(mat[i][j],end =" ")
            
mat = [[2, 1, 4, 3],
       [1, 2, 3, 2],  
       [3, 6, 2, 3],  
       [5, 2, 5, 3]]
dictinctElement(mat)