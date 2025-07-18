import numpy as np
ar_name=np.array([[1,2,3,4],[5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
print(ar_name)
print()
print(ar_name[1:, :])
print()
print(ar_name[:, 0:3])
print()
print(ar_name[1:3,0:2])
print()
print(ar_name[ : ,1:3])
print()
print(ar_name[1:3, : ])
