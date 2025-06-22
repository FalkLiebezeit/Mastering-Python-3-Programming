#01_koordinaten.py
from vpython import *
h=10. #Hoehe
b=10. #Breite
t=10. #Tiefe
scene.title="<h2>Koordinatensystem von VPython</h2>"
scene.width=scene.height=600
scene.background=color.white
scene.center=vector(0,0,0)
scene.range=1.5*b
x0=vector(-b,0,0)
y0=vector(0,-h,0)
z0=vector(0,0,-t)
#x-Achse ist rot
arrow(pos=x0,axis=vector(2*b,0,0),shaftwidth=0.15,color=color.red)
#y-Achse ist grün
arrow(pos=y0,axis=vector(0,2*h,0),shaftwidth=0.15,color=color.green)
#z-Achse ist blau
arrow(pos=z0,axis=vector(0,0,2*t),shaftwidth=0.15,color=color.blue)
label( pos=vec(b,-1,0),text="x",height=30,box=False,opacity=0)
label( pos=vec(-1,h,0),text="y",height=30,box=False,opacity=0)
label( pos=vec(-1,0,t),text="z",height=30,box=False,opacity=0)
points(pos=vector(5,5,0))
scene.caption="\nRechte Maustaste drücken und ziehen"
