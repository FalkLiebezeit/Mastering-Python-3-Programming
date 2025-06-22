#18_pendel.py
from vpython import *
y0=-5.  #Verschiebung y-Achse
b=5.    #Breite der Decke
l=8.    #Länge des Pendels
phi=45. #Auslenkung
r=0.5   #Radius der Kugel
scene.width=600
scene.height=600
scene.center =vector(0,y0,0)
scene.range=1.5*b
scene.background = color.white
box(size=vector(b,b/20.,b/2.),color=color.gray(0.8)) #Decke
stange=cylinder(axis=vector(0,l,0),radius=0.05)
masse = sphere(radius=r,color=color.red)
masse.pos=vector(0,stange.pos.y,0)
g=9.81   #Erdbeschleunigung
w02=g/l  #Quadrat der Kreisfrequenz
phi=radians(phi) 
w=0.      #Anfangswinkelgeschwindigkeit
dt=0.02   #Zeitschrittweite
while True:
    rate(100)
    phi=phi+w*dt
    w=w-w02*sin(phi)*dt #-0.001*w
    x= l*sin(phi)
    y=-l*cos(phi)
    stange.axis=vector(x,y,0)
    masse.pos  =vector(x,y,0)


