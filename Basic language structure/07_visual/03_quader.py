#03_quader.py
from vpython import *
scene.title="<h2>Quader und andere Körper</h2>"
scene.autoscale=True
scene.background=color.white
scene.width=600
scene.height=600
scene.center=vector(0,0,0)
#x0,y0,z0
p=vector(0,0,0)
#Ausrichtung 
a=vector(1,0,0)
#Abmessungen: Breite, Höhe, Tiefe
dim=vector(40,20,10)
scene.range=30
#Drehung
d=vector(0,0,0)
c=color.gray(0.5)
box(pos=p,axis=a,size=dim,up=d,color=c)
#cone(pos=vector(-5,0,0),axis=vector(10,0,0),radius=5,color=c)
#ellipsoid(pos=vector(0,0,0),axis=vector(1,0,0),size=vector(10,5,5),color=c)
#pyramid(pos=vector(0,-5,0),axis=vector(0,1,0),size=vector(10,12,12),color=c)
#ring(pos=vector(0,0,0),axis=vector(0,0,1),radius=10,thickness=3,color=c)
scene.caption="\nRechte Maustaste drücken und das Objekt drehen"


