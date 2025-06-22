#L_10_04.py
from sympy.logic import simplify_logic
from sympy import symbols
x1, x2, x3 = symbols('x1 x2 x3')
y=(~x1 & x2 & ~x3)|(x1 & ~x2 & ~x3 )|(x1 & x2 & ~x3)
print(simplify_logic(y))