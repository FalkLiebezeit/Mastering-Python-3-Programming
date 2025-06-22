#21_federpendel_gekoppelt.py
from vpython import *
y0=-5. #Verschiebung y-Achse
b=10.  #Breite der Decke
r=1.2  #Radius der Masse
l=0.9*y0 #Federlänge
c1=1.   #Federkonstante
m1=1.   #Masse der Kugel
c2=1.
m2=1.
scene.width=600
scene.height=800
scene.center =vector(0,2*y0,0)
scene.background = color.white
box(pos=vector(0,b/40.,0),size=vector(b,b/20.,b/2.),color=color.gray(0.8)) #Decke
feder1 = helix(pos=vector(0,0,0),axis=vector(0,l,0),
               color=color.yellow,radius=0.5*r,thickness=0.2,coils=10)
masse1 = sphere(pos=feder1.pos,radius=r, color=color.red)
feder2 = helix(pos=vector(0,l,0),axis=vector(0,l,0),
               color=color.green,radius=0.5*r,thickness=0.2,coils=10)
masse2 = sphere(pos=vector(0,2*l,0),radius=r, color=color.blue)
y1=-0.6*l #Auslenkung
y2=0
v1=v2=0   #Anfangsgeschwindigkeit
lk=l-r
dt=0.02
while True:
    rate(50)
    y1=y1 + v1*dt
    v1=v1-(c1+c2)/m1*y1*dt+c2/m1*y2*dt#-0.05*v1*dt
    y2=y2 + v2*dt
    v2=v2-c2/m2*(y2-y1)*dt #-0.05*v2*dt
    feder1.axis=vector(0,y1+l,0)
    masse1.pos =vector(0,y1+lk,0)
    feder2.axis=vector(0,y1+y2+l,0)
    feder2.pos.y =masse1.pos.y
    masse2.pos =feder2.pos+vector(0,y1+y2+lk,0)
   


