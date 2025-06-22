#06_kugeln1.py
from vpython import *
scene.width=600
scene.hight=600
scene.background=color.white
x0=5.
y0=5.
z0=5.
R1=1.
R2=0.25
#Mitte
sphere(pos=vector(0,0,0),radius=R1,color=color.red)
#oben
sphere(pos=vector(0,y0,0),radius=R2,color=color.blue)
#unten
sphere(pos=vector(0,-y0,0),radius=R2,color=color.blue)
#links
sphere(pos=vector(-x0,0,0),radius=R2,color=color.blue)
#rechts
sphere(pos=vector(x0,0,0),radius=R2,color=color.blue)
#hinten
sphere(pos=vector(0,0,-z0),radius=R2,color=color.blue)
#vorne
sphere(pos=vector(0,0,z0),radius=R2,color=color.blue)
label( pos=vec(0,0,0), text="O",height=30,box=False,opacity=0)
sphere(pos=vector(x0/2,0,0),radius=R2,color=color.blue)
sphere(pos=vector(-x0/2,0,0),radius=R2,color=color.blue)
