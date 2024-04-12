import numpy as np
from numpy.linalg import inv, det, solve
from time import process_time

def cast1(A, b):
    start = process_time()

    x = solve(A, b)

    stop = process_time()

    xtime = stop-start

    print(x)

    start = process_time()

    deter = det(A)
    A[:, 0] = b
    deter1 = det(A)

    stop = process_time()

    cramtime = stop-start

    start = process_time()

    invA = inv(A)

    stop = process_time()

    atime = stop-start

    print(A)
    print(f"x:{x}, {xtime}")
    print(f"cramer: {deter1/deter}, {cramtime}")
    print(f"invA:{invA}, {atime}")
def iteracni(A, b, hodnoty,rozdil=0, p=1):
    L = np.tril(A, k = -1)
    U = np.triu(A, k = 1)
    D = np.diag(np.diag(A))

    

    if det(A) != 0 and det(D) != 0:
        inverz = inv(D)
        x0 = np.ones(len(A))
        x1 = np.zeros(len(A))

        for i in range(10000):
            
            #x1 = np.matmul(inverz, (b-np.matmul((L + U),x0)))
            x1 = x1 + p*(np.matmul(inv(D + L), b-np.matmul(U, x0)) - x1)
            if all(x1 == x0):
                print("konec")
                break
            elif np.absolute(x1[0]+x0[0])>hodnoty*2:
                break
            x0 = x1
            print(f"iterace {i}: {x1}")
        else:
            print("nefunguje to")
        print(solve(A,b))
    else:
        print("matice je lin zavisla")


N = 2
hodnoty = 20

A = np.random.randint(hodnoty, size = (N, N))
b = np.random.randint(hodnoty, size = (N))

iteracni(A,b,hodnoty)