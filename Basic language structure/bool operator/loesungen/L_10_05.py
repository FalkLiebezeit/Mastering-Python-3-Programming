#L_10_05.py
from sympy.logic import simplify_logic
from sympy import symbols
m1, m2, m3 = symbols('m1 m2 m3')
y=(m1 & ~m2 & m3)|(~m1 & m2 & m3 )|(m1 & m2 & m3)
print(simplify_logic(y))