import numpy as np
from random import randint
mez = 3

matice = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matice-=1

z = np.full((3,3), np.e)
l = np.full((4,4), np.arange(4))

arr1 = np.arange(mez, dtype=np.int64)
arr2 = np.arange(mez, dtype=np.int64)

print(-matice,matice>3, z, l)


print(np.dot(arr1, arr2))


def quicksort(seznam):
    if len(seznam) < 2: return seznam
    pivot = seznam.pop()
    return quicksort([prvek for prvek in seznam if prvek<=pivot]) + [pivot] + quicksort([prvek for prvek in seznam if prvek>pivot]) 

print(quicksort([8,1,4,5,6,7,2,9,00,1,254,2,74,6,15]))