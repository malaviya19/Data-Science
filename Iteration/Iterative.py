# Author: Malaviya Nerumalan
# Date: January 20, 2020
# Purpose: To find an approximate solution to a given function
#********************************************************************************************************************************
import FunctionIteration as fi


#*********************************************************************************************************************************
# Author: Malaviya Nerumalan
# Date: January 20, 2020
# Purpose: To find an approximate solution given the starting x value, functions and error values
# Parameters: starting x value, maximum iterations, residual error, and error residual
# Return: approximate x value
#**********************************************************************************************************************************
def iterative(x,kmax, resT, errT):
    c = False

    for i in range (kmax):
        print("\n" + str(i))
        # any initial point from (0,2] xk converges
        xk = fi.gx(x)
        print("x: " + str(xk))
        # error between the x values
        err = abs(xk-x)
        print("error: " + str(err))
        # residual between the y values
        res = abs(fi.fx(xk)-fi.fx(x))
        print("residual: " + str(res))
        x = xk

        if (err < errT and res < resT):
            print("\nConverged")
            c = True
            break

    if (c == False):
        print("\nMaximum iterations reached, not converged")

    return xk,err,res
