# Author: Malaviya Nerumalan
# Date: January 20,2020
# Purpose: To find an approximate solution to a function
#**********************************************************************************************************************
import FunctionIteration as fi

#**********************************************************************************************************************
# Author: Malaviya Nerumalan
# Date: January 20,2020
# Purpose: To find an approximate solution using recursion
# Parameters: starting x value, maximum iterations, error, and residual
#**********************************************************************************************************************
def recursive(x,kmax,errT,resT):
    xk = fi.gx(x)
    print("\nx: " + str(xk))
    # error between the x values
    err = abs(xk-x)
    print("error: " + str(err))
    # residual between the y values
    res = abs(fi.fx(xk)-fi.fx(x))
    print("residual: " + str(res))

    if (kmax > 0):
        if (err > errT and res > resT):
            recursive(xk,kmax-1,errT,resT)
        else:
            print("\nConverged with approximate value of " + str(xk) + "\nerror: " + str(err) + "\nresidual: " + str(res))
    else:
        print("Maximum iterations reached, not converged")

    return xk,err,res
