# Search in row wise and column wise sorted matrix

def search(matrix, target):

    i = 0     
    j = len(matrix) - 1
    
    while ( i < len(matrix) and j >= 0 ):
     
        if (matrix[i][j] == target):
            return (i, j)
     
        if (matrix[i][j] > target):
            j -= 1
             
        else:
            i += 1
     
    return -1


matrix = [[10, 20, 30, 40], [15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]]
print(search(matrix, 15))
