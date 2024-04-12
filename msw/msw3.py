import numpy as np
from numpy.linalg import inv, det
from random import randint
from time import process_time

#a = np.mat("[1,2,3;4,5,6;7,8,9]")

a = np.array([[3, 2, 1, 5], [2, 3, 1, 1], [2, 1, 3, 11]])
b = np.mat("[1,2,1;3,1,1;4,1,1]")

print(a)
print(a[:, :3])

deter = det(a[:, :3])
a[:, [3, 0]] = a[:, [0, 3]]
deter1 = det(a[:, :3])

print(a)
print(deter1/deter)