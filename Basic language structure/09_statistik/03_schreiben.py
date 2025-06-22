#03_schreiben.py
import numpy as np
n=50
sollwert=50
s=1
werte=np.random.normal(sollwert,s,size=n)
rwerte=np.around(werte,decimals=2)
np.savetxt("daten.txt", werte,fmt="%4.2f")
print("normalverteilte Werte:")
print(rwerte)
print("Typ der Werte:",type(werte))

