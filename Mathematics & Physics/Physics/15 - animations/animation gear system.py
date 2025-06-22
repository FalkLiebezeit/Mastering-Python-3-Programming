#39_animation_getriebe.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.patches import Polygon
m=0.5   #Modul
i=2     #Übersetzungsverhältnis
d1=8    #mittlerer Durchmesser
d2=i*d1
a=(d1+d2)/2
z1=d1/m #Anzahl der Zähne
z2=i*z1
h=13*m/6 #Zahnhöhe
c=0.2*m  #Zahnspiel
i=complex(0,i)
x1=1/7
x2=1/3
zahnform=np.array([-x2,-x1,x1,x2])
frames=60
xmax=-11/16*d2,22/16*d2
ymax=-10/16*d2,10/16*d2
#Funktionsdefinition für ein Zahnrad
def zahnrad(d,z,h):
    r=d/2
    alpha=2*np.pi/z #Winkelbereich
    sektor=zahnform*alpha
    zahnradausschnitt=np.array([r-h/2,r+h/2,r+h/2,r-h/2])-c
    zahn=zahnradausschnitt*np.exp(1j*sektor)
    return np.outer(np.exp(1j*alpha*np.arange(z)),zahn).ravel('C')
#Zahnrad-Objekte erzeugen
zr1=zahnrad(d1,z1,h)
zr2=zahnrad(d2,z2,h)*np.exp(1j*np.pi/z2)
schritt=2*np.pi/(z2*frames)
fig=plt.figure(figsize=(6,4))
ax=fig.add_axes([-0.2,-0.1,1.2,1.2])
bild=[]
for k in range(frames):
    zr1=zr1*np.exp(-i*schritt) #rechts drehend
    zr2=zr2*np.exp(1j*schritt) #links drehend
    P1=Polygon(zr1.view(float).reshape(zr1.size,2),color='grey')
    P2=Polygon(zr2.view(float).reshape(zr2.size,2)+[a,0],color='k')
    bild.append([ax.add_patch(P1),ax.add_patch(P2)])
an=ani.ArtistAnimation(fig,bild,interval=20,blit=True)
ax.set_aspect("equal")
ax.set_xlim(xmax)
ax.set_ylim(ymax)
plt.show()
