#To print the transpose of a given 2d array(90degree clockwise rotation)
#review once again

def transpose(list1):
    for i in range(len(list1)):
        for j in range(i,len(list1)):
            list1[i][j],list1[j][i] = list1[j][i],list1[i][j]
    
    for row in list1:
        row.reverse()
    return list1
my_list = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(my_list))