import numpy as np
from matplotlib import pyplot as plt

def mean(x):
    s = 0
    for i in x:
        s+=i
    return s*len(x)**(-1)

def SUM(pro):
    s = 0
    for i in pro:
        s+=i

    return s

def regression(x, y):

    if len(x) == len(y):

        n = len(x)
        
        xb, yb = mean(x), mean(y)

        varx, vary = [(i-xb) for i in x], [(i-yb) for i in y]
        pro = []
        
        for i in range(n):
            pro.append(varx[i]*vary[i])

        sq = [i**2 for i in varx]

        b = SUM(pro)*SUM(sq)**(-1)

        a = yb - b*xb

        print a, b

        plt.scatter(x, y)

        t = np.arange(min(x)-1, max(x)+1, 0.01)
        f = a + b*t

        plt.plot(t, f)
        plt.title("y = "+str(b)+"*x + ("+str(a)+")")
        plt.ylabel('y')
        plt.xlabel('x')
        plt.show()
        
