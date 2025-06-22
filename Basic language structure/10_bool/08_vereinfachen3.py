#08_vereinfachen3.py
from sympy.logic import simplify_logic
from sympy import symbols
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
y1 = ( x1 | ~x2 |  x3 | ~x4)  
y2 = ( x1 | ~x2 | ~x3 |  x4)
y3 = ( x1 | ~x2 | ~x3 | ~x4)
y4 = (~x1 |  x2 |  x3 | ~x4)
y5 = (~x1 | ~x2 |  x3 |  x4)
y6 = (~x1 | ~x2 |  x3 | ~x4)
y=y1 & y2 & y3 & y4 & y5 & y6
V=simplify_logic(y)
print("y = ",V)