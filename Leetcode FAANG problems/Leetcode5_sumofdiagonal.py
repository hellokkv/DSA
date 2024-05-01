#write a function such that it returns he sum of diagonal of a 2d matrix

def diagonal_sum(matrix):
    total=0
    for i in range(len(matrix)):
        total+=matrix[i][i]
    return total
myList2D = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonal_sum(myList2D))