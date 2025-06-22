#L07_01.py
#4 Kugeln im Raum
from vpython import *
scene.background=color.white
scene.width=scene.hight=600
R=1.
r=sqrt(2)*R
x=vector(r,0,0)
y=vector(0,r,0)
z=vector(0,0,r)
sphere(pos=-x,radius=R,color=color.red)
sphere(pos=x,radius=R,color=color.red)
sphere(pos=y,radius=R,color=color.green)
sphere(pos=-y,radius=R,color=color.green)
sphere(pos=z,radius=R,color=color.blue)
sphere(pos=-z,radius=R,color=color.cyan)