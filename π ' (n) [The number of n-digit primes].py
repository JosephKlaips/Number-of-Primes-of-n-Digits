import sympy
import random
from sympy import *
import matplotlib.pyplot as plt

n = 15

#plotting the points S
X = []
Y = []
#v = len(actualSum(primeList(n)))
plt.ylabel('π (n)')
plt.xlabel('n')
x = 1
y_1 = 0;
y_2 = primepi(10**0);
while x <= n:
    #y = x/primeomega(x)
    z = x - 1
    y_1 = y_2
    y_2 = primepi(10**x)
    y = y_2 - y_1
    Y.append(y)
    X.append(x)
    x = x + 1


#while v <= n:
    #v = v + 1
    #color='none', linestyle = 'dashed', linewidth = 20,
    #marker = 'o', markersize = 8, markerfacecolor = 'blue', markeredgecolor = 'blue'


#giving a title to my graph
plt.scatter(X, Y)
#plt.plot(X, Y)
plt.title("π'(n) vs n")
#function to show the plot
#plt.grid()
plt.show()
