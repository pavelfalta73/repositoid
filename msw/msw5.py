import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

def f(x):
    return -x**3 + 10*x**2 - 3*x + 6

def linter(x, a, b):
    return f(a) + (f(b)-f(a))/(b-a)*(x-a)

def interpo():
    start = 0
    end = 10
    kolik = 50

    x = np.linspace(start, end, kolik)

    y = f(x)

    x_interpolace = []
    y_interpolace = []

    for i in range(len(x)-1):
        x1 = x[i]
        x2 = x[i+1]
        rozdeleni_x1_x2 = np.linspace(x1, x2, 5)

        y_x1_x2 = linter(rozdeleni_x1_x2, x1, x2)

        x_interpolace.extend(rozdeleni_x1_x2)
        y_interpolace.extend(y_x1_x2)

    plt.plot(x_interpolace, y_interpolace, "y-")
    plt.plot(x, y, "ro")

    plt.show()

    phi = interpolate.interp1d(x, f(x))
    xnew = np.arange(0, 10, 0.2)
    ynew = phi(xnew)
    
    plt.title("1-D Interpolation")
    plt.plot(x, f(x), 'ro', xnew, ynew, 'g-')
    plt.show()


def vander(a,y):
    N = 10
    X = np.vander(a, increasing=True)
    a = np.linalg.solve(X,y)
    xs = np.linspace(0,N-1,200)
    ys = sum([a[k]*xs**k for k in range(0,N)])
    plt.plot(x,y,'r.',xs,ys)
    plt.show()
        
def newton(x):#TODO
    print(x[1:],x[:-1],len(x))
    if len(x) == 2:
        return (f(x[0])-f(x[1]))/(x[0]-x[1])
    else:
        return (newton(x[1:]) - newton(x[:-1]))/(x[0]-x[len(x-1)])

# Define a function to calculate divided differences recursively
def divided_diff_recursive(x, y):
    # Base case: if there's only one element in y, return that element
    if len(y) == 1:
        return y[0]
    else:
        # Recursive calculation of divided difference
        return (divided_diff_recursive(x[1:], y[1:]) - divided_diff_recursive(x[:-1], y[:-1])) / (x[-1] - x[0])

# Function to calculate divided differences matrix
def divided_diff(x, y):    
    n = len(y)
    # Initialize matrix to store divided differences
    coef = np.zeros([n, n])
    coef[:,0] = y
    # Calculate divided differences for each order
    for j in range(1, n):
        for i in range(n - j):
            # Use the recursive function to calculate divided differences
            coef[i][j] = divided_diff_recursive(x[i:i+j+1], y[i:i+j+1])
    return coef

# Function to perform Newton polynomial interpolation
def newton_poly(coef, x_data, x):
    n = len(x_data) - 1 
    p = coef[n]
    # Evaluate polynomial for each x value
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

# Sample data
start = 1
end = 10
kolik = 10

# Generate x values
x = np.linspace(start, end, kolik)
# Sample function, you can replace this with your own function f(x)
y = f(x)

# Calculate coefficients using divided differences
a_s = divided_diff(x, y)[0, :]

# Generate new x values for interpolation
x_new = np.arange(x[0], x[-1], .1)
# Interpolate y values using Newton polynomial interpolation
y_new = newton_poly(a_s, x, x_new)

plt.plot(x, y, 'ro', label='Original data')
plt.plot(x_new, y_new, label='Interpolated curve')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Newton Interpolation')
plt.legend()
plt.show()





# phi = interpolate.interp1d(x, f(x))
# xnew = np.arange(1, 10, 0.2)
# ynew = phi(xnew)

# plt.title("1-D Interpolation")
# plt.plot(x, f(x), 'ro', xnew, ynew, 'g-')
# plt.show()