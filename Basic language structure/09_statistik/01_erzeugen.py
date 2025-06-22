#01_erzeugen.py
import numpy as np
n=10
sollwert=50
s=1
werte=np.random.normal(sollwert,s,size=n)
rwerte=np.around(werte,decimals=2)
print("normalverteilte Werte:")
print(werte)
print("gerundete Werte:")
print(rwerte)
print("Typ der Werte:",type(werte))