import Iterative
import Recursion

x = 1
k = 50
res = 0.00001
err = 0.00001

#y,errT,resT = Iterative.iterative(x,k,res,err)
#print("Approximate solution: " + str(y) + "\nerror: " + str(errT) + "\nresidual: " + str(resT))

Recursion.recursive(x,k,res,err)
