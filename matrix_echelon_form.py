# import sympy
from sympy import *

M = Matrix([[0,2,3,-4,1],[0,0,2,3,4],[2,2,-5,2,4],[2,0,-6,9,7]])


# Use sympy.rref() method
M_rref = M.rref()
print(M_rref)
