#22_doppelpendel.py
from vpython import *
phi1=radians(-5.)
phi2=radians(5.)
b=12.   #Breite der Decke
y0=-b/2.#Verschiebung y-Achse
a=b/2.  #Abstand der Pendel
l=0.9*b #Länge der Pendel
r=b/15. #Radius der Kugeln
m=10.   #Masse der Kugeln
c=4.5   #Federkonstante
scene.width=600
scene.height=600
scene.center=vector(0,y0,0)
scene.range=0.8*b
scene.background = color.white
box(size=vector(b,b/20.,b/4.),color=color.gray(0.8)) #Decke
stange1=cylinder(axis=vector(0,l,0),radius=0.05)
stange1.pos=vector(-a/2.,0,0)
stange2=cylinder(axis=vector(0,l,0),radius=0.05)
stange2.pos=vector(a/2.,0,0)
masse1 = sphere(radius=r,color=color.red)
masse2 = sphere(radius=r,color=color.blue)
feder=helix(axis=vector(a,0,0),radius=0.4)
feder.thickness=0.1
feder.coils=10
g=9.81   #Erdbeschleunigung
w02=g/l  #Pendelfequenz
k=c/m    #Federfrequenz
w1=w2=0  #Winkelgeschwindigkeit
dt=0.02
while True:
    rate(100)
    phi1=phi1+w1*dt
    w1=w1-w02*phi1*dt+k*(phi2-phi1)*dt -0.05*w1*dt
    phi2=phi2+w2*dt
    w2=w2-w02*phi1*dt-k*(phi2-phi1)*dt -0.05*w2*dt
    x1= l*sin(phi1)
    y1=-l*cos(phi1)
    x2= l*sin(phi2)
    y2=-l*cos(phi2)
    stange1.axis=vector(x1,y1,0)
    masse1.pos  =vector(x1-a/2.,y1,0)
    stange2.axis=vector(x2,y2,0)
    masse2.pos  =vector(x2+a/2.,y2,0)
    feder.pos=masse1.pos+vector(r,0,0)
    feder.axis.x=x2-x1+a-2*r
    feder.axis.y=y2-y1
   



