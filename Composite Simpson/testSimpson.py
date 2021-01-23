# Author: Malaviya Nerumalan, 100701778
# Date: March 31, 2020
# Purpose: To determine the composite Simpson function given the If function
#***************************************************************************************************************************************************
from compositeSimpson import *
import math
from scipy.integrate import quad

#***************************************************************************************************************************************************
# Author: Malaviya Nerumalan, 100701778
# Date: March 31, 2020
# Purpose: To determine the function value given an x value
# Parameters: x value
# Return: f(x)
#****************************************************************************************************************************************************
def fx(x):
    return (math.exp(-(x**3)))
#***************************************************************************************************************************************************
# Author: Malaviya Nerumalan, 100701778
# Date: March 31, 2020
# Purpose: To determine the area of the function given f(x) and (a,b) values
# Parameters: f(x),a,b
# Return: the area of the function
#****************************************************************************************************************************************************
def If(f,a,b):
    return quad(f,a,b)


M = 4
a = 0
b = 1
I =  compositeSimpson(fx,a,b,M)
print(I)

#while (True):
#    M = M + 1
#    I =  compositeSimpson(fx,a,b,M)
#    err = abs(If(fx,a,b)[0] - I)
#    print("%d %e" % (M,err))
#    if (err <= 10e-12):
#        break
