#19_federpendel.py
from vpython import *
y0=-5. #Verschiebung y-Achse
b=8.   #Breite der Decke
l=0.8*y0 #Länge der Feder
r=1.2  #Radius der Masse
c=1.1  #Federkonstante
m=1.5  #Masse der Kugel
scene.width=600
scene.height=600
scene.center =vector(0,y0,0)
scene.background = color.white
box(pos=vector(0,b/40.,0),size=vector(b,b/20.,b/2.),color=color.gray(0.8)) #Decke
feder=helix(axis=vector(0,l,0),radius=0.6,color=color.yellow)
feder.thickness=0.2
feder.coils=8
masse=sphere(pos=feder.pos,radius=r,color=color.red)
w02=c/m   #Quadrat der Kreisfrequenz
y=-0.6*l  #Auslenkung
v=0.      #Anfangsgeschwindigkeit
dt=0.02
while True:
    rate(100)
    y=y+v*dt
    v=v-w02*y*dt
    feder.axis=vector(0,y+l,0)
    masse.pos =vector(0,y+l-r,0)
   

