#L_10_06.py
from sympy.logic import simplify_logic
from sympy import symbols
D, C, B, A = symbols('D C B A')
 
c2 =( D| C|~B| A)
c10=(~D| C|~B| A)
c11=(~D| C|~B|~A)
c12=(~D|~C| B| A)
c13=(~D|~C| B|~A)
c14=(~D|~C|~B| A)
c15=(~D|~C|~B|~A)                 
c=c2 & c10 & c11 & c12 & c13 & c14 & c15 
print("c = ",simplify_logic(c))
'''
Loesung aus Fachliteratur (Beuth, Digitaltechnik)
mit ODER-Normalform ermittelt
c= A | ~B | C
'''
