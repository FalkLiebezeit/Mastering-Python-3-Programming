import numpy as np
A=np.array([1, 2, 3])
B=np.array([4, 5, 6])
print("Vektor      A:",A)
print("Vektor      B:",B)
print("Summe     A+B:",A+B)
print("Produkt   A*B:",A*B)
print("Kreuzprodukt :",np.cross(A,B))
print("Skalarprodukt:",np.dot(A,B))