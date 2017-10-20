# test script
import random as r
import regression
# dataset x
x = [r.randrange(-2, 2, 0.01, float) for i in range(10)]
# dataset y
y = [r.randrange(-1, 1, 0.01, float) for i in range(10)]

regression.regression(x, y)
