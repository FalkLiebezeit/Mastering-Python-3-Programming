#L07_03.py
#Zylinder durchdringt Kugel
from vpython import *
scene.background=color.white
scene.width=scene.hight=600
R=10.
r=5
x=vector(r,0,0)
y=vector(0,r,0)
z=vector(0,0,r)
sphere(radius=R,color=color.gray(0.5),opacity=0.5)
cylinder(pos=vec(-15,0,5),axis=vec(30,0,0),radius=5,color=color.blue)
