import numpy as np
np_array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(np_array)
print()
new_array = np.delete(np_array,0,axis=0)
print(new_array)
                    