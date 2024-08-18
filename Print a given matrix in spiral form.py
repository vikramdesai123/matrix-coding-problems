# Print a given matrix in spiral form

def spiralMatrix(mat):
    top = 0 
    bottom = len(mat)-1
    right = len(mat[0])-1
    left = 0 
    
    while(top<=bottom and left<=right):
        for i in range(left,right+1):
            print(mat[left][i],end=" ")
        top += 1 
        
        for i in range(top,bottom+1):
            print(mat[i][bottom],end=" ")
        right -= 1 
        
        for i in range(right,left-1,-1):
            print(mat[bottom][i],end=" ")
        bottom -= 1 
        
        for i in range(bottom,top-1,-1):
            print(mat[i][left],end=" ")
        left += 1 
        

mat = [[1,  2, 3, 4],
       [5,  6, 7, 8],
       [9, 10,11,12],
       [13,14,15,16]]
spiralMatrix(mat)