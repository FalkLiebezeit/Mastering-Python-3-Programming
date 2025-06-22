#09_siebensegment.py
from sympy.logic import simplify_logic
from sympy import symbols
D, C, B, A = symbols('D C B A')

a=( D|C|B|~A) & (D|~C|B|A) & (D|~C|~B|A)  
b=( D|~C|B|~A)&(D|~C|~B|A) 
c=( D|C|~B|A)                 
d=( D|C|B|~A) & (D|~C|B|A) & (D|~C|~B|~A) 
e=(~D&~C&~B&~A)|(~D&~C&B&~A)|(~D&C&B&~A)|(D&~C&~B&~A) 
f=(D|C|B|~A) & (D|C|~B|A) & (D|C|~B|~A) & (D|~C|~B|~A) 
g=(D|C|B|A) & (D|C|B|~A) & (D|~C|~B|~A) 

print("a = ",simplify_logic(a))
print("b = ",simplify_logic(b))
print("c = ",simplify_logic(c))
print("d = ",simplify_logic(d))
print("e = ",simplify_logic(e))
print("f = ",simplify_logic(f))
print("g = ",simplify_logic(g))
