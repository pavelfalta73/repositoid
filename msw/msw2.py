import matplotlib.pyplot as plt
import numpy as np


# def moje_funkce(n, min=0, max=100):

#     x = np.linspace(min, max, n)
#     y = np.sin(x)
#     return x,y

# x, y = moje_funkce(100,0,2*np.pi)

# y1 = 2*y


# plt.figure(figsize=(8,8), dpi=144)

# plt.subplot(2, 2, 1)
# plt.plot(x,y, "ro", label="prvni sinus", markersize=1)
# plt.ylabel("sin(x)")
# plt.xlabel("x")
# plt.legend()
# plt.title("graf 1")

# plt.subplot(2, 2, 2)
# plt.plot(x, y1, "-.g", label ="druhy sinus")
# plt.ylabel("sin(x)")
# plt.xlabel("x")
# plt.legend()
# plt.title("graf 2")

# plt.subplot(2, 1, 2)
# #plt.plot(x, y1, "b", label ="treti sinus")
# plt.plot(x, y1, "red", x, y, "blue")   
# plt.fill(x,y1,"red",x,y, "yellow", alpha=0.3)
# plt.ylabel("sin(x)")
# plt.xlabel("x")
# plt.legend()
# plt.title("graf 3")



# plt.show()


# index1 = np.linspace(0,50,50)
# index2 = np.linspace(25,50,25)
# cena = [randint(20,30) for i in range(len(index1))]
# predpoklad = [i  + randint(-5,5) for i in cena[len(cena)//2:]]

# width = 1.00                    
 
# plt.bar(index1, cena, width, color='green', edgecolor='black', label='cena plynu')

# plt.bar(index2, predpoklad, width, color='red', edgecolor='black', label='predpoklad ceny', alpha=0.5) 

# plt.grid(True)                

# plt.legend()

# plt.show()

N = 1_000_000

y = np.random.rand(N)
y2 = np.random.randn(N)
# print(sorted(y))

plt.subplot(1,2,1)
plt.hist(y,bins=30,edgecolor="black",range=None,density=True)
plt.subplot(1,2,2)
plt.hist(y2,bins=30,edgecolor="black",range=None,density=True)

plt.show()