# Author: Malaviya Nerumalan, 100701778
# Date: March 31, 2020
# Purpose: To determine the composite simpson function of an If function
#***************************************************************************************************************************************************


#***************************************************************************************************************************************************
# Author: Malaviya Nerumalan, 100701778
# Date: March 31, 2020
# Purpose: To determine the composite simpson function given f(x), (a,b) values, and the number of intervals
# Parameters: f(x), (a,b) values, M intervals
# Return: composite simpson function
#****************************************************************************************************************************************************
def compositeSimpson(f,a,b,M):
    I = 0
    xl = []
    xk = []
    h = (b-a)/M

    for l in range(M+1):
        xl.append(a+l*h)

    for k in range(1,M+1):
        xk.append((xl[k-1]+xl[k])/2)

    # composite Simpson function
    for k in range(1,M+1):
        I = I + f(xl[k-1]) + 4*f(xk[k-1]) + f(xl[k])

    I = (h/6)*I

    return I
