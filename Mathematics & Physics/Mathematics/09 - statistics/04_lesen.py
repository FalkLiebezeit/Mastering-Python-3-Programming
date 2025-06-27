#04_lesen.py
import numpy as np
werte = np.loadtxt("daten.txt")
n=len(werte)
print("geladene Werte:")
print(werte)
print("Anzahl der Werte:",n)
print("Typ der Werte:",type(werte))

