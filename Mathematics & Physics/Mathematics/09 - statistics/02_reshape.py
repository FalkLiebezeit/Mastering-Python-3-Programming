#02_reshape.py
import numpy as np

zeilen=5
spalten=10
n=spalten*zeilen
sollwert=10
s=1

werte=np.random.normal(sollwert,s,size=n)
rwerte=np.around(werte,decimals=2)
swerte=np.sort(rwerte)
tabelle=np.reshape(swerte,(zeilen,spalten),order='F')

print("Messwerte:\n",swerte)
print("Tabelle:\n",  tabelle)
print("Minimaler Wert:", np.amin(rwerte))
print("Maximaler Wert:", np.amax(rwerte))


