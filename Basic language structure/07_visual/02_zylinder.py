#02_zylinder.py
from vpython import *
scene.title="<h2>Zylinder</h2>"
#scene.autoscale=True
scene.background=color.white
scene.width=600
scene.height=600
scene.center=vector(0,0,0)
scene.range=40
#Position: x0,y0,z0
p=vector(-20,0,0)
#Ausrichtung und Länge
a=vector(40,0,0)
r=10.  #Radius
#col=color.gray(0.5) 
#red, green, blue
col=vector(1,0,0)
cylinder(pos=p,axis=a,radius=r,color=col,opacity=0.5)
#Länge, Höhe, Breite
#cylinder(pos=p,size=vector(40,20,20),color=col)
scene.caption="\nRechte Maustaste drücken und das Objekt drehen"
