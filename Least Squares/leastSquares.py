# Author: Malaviya Nerumalan
# Date: March 23, 2020
# Purpose: To create the least squares interpolation of given x and y values
#*****************************************************************************************************************************************

import numpy as np
import matplotlib.pyplot as plt

#******************************************************************************************************************************************
# Author: Malaviya Nerumalan
# Date: March 23, 2020
# Purpose: To determine the x values for the least squares interpolant
# Parameters: x values, y values, number of x values
# Return: solutions to the least squares interpolant
#******************************************************************************************************************************************
def leastSquares(x,y,n):
    # Vandermonde matrix
    a = np.vstack([x,np.ones(n)])
    aT = np.transpose(a)
    b = np.array(y)
    m,c = np.linalg.lstsq(aT,b,rcond=None)[0]
    x = np.array([m,c])

    return x

#******************************************************************************************************************************************
# Author: Malaviya Nerumalan
# Date: March 23, 2020
# Purpose: To determine the y value of the least squares interpolant for the given x value
# Parameters: x values, least squares interpolant
# Return: y value of the least squares interpolant
#******************************************************************************************************************************************
def fx(x,xs):
    return xs[0]*x + xs[1]

#******************************************************************************************************************************************
# Author: Malaviya Nerumalan
# Date: March 23, 2020
# Purpose: To determine the mean square residual of the least squares interpolant
# Parameters: x values, y values, number of x values
# Return: the mean square residual
#******************************************************************************************************************************************
def leastSquaresError(x,y,n):
    xs = leastSquares(x,y,n)
    r = 0
    for i in range (n):
        r = r + (fx(x[i],xs)-y[i])**2

    return r


x = [-2,0.25,0.9,1]
y = [2.23,4.29,5.12,6.3]
# number of (x,y) values
n = 4
xs = leastSquares(x,y,n)
r = leastSquaresError(x,y,n)
ys = np.zeros(n)
print("x:",xs)
print("error:",r)

# y values of the interpolant
for i in range(n):
    ys[i] = fx(x[i],xs)

# plot of the interpolant
plt.scatter(x,ys,color='green')
plt.plot(x,ys,color='green')
plt.scatter(x,y,color='red')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
