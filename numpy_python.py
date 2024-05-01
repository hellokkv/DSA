import numpy as np
np_arrays = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(np_arrays)

def traverse(np_arrays):
    for i in range(len(np_arrays)):
        for j in range(len(np_arrays[0])):
            print(np_arrays[i][j],end=',')
traverse(np_arrays)