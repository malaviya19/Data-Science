# Test script for Gauss elimination. L. van Veen, Ontario Tech U, 2020.
import numpy as np
from Gauss import *
# Set test matrix and right hand side:
A = np.array([[1.,2.,3.],[4.,-4.,9.],[-2.,4.4,5.]])
y = np.array([[3.],[5.],[-9.2]])
# Compute the upper triangular system resulting from Gauss elimination:
B = Gauss(A,y)
print(B)
# Now find the solution to A x = y by back substitution: 
x = BackSub(B)
print(x)
# Print the residual vector A x - y, which should be zero up to round-off error:
print("If the elements of the following vector are not zero (up to round-off error), there is something wrong:")
print(np.dot(A,x)-y)

