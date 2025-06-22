#07_02.py
#Parallelogramm
from vpython import *
scene.width=600
scene.height=600
scene.background=color.white
r=5. 
scene.center=vector(0,0,0)
scene.range=1.8*r
x1=-5
y1=2
x2=5
y2=2
x3=5
y3=-2
x4=-5
y4=-2
b=1 #Verschiebung

k1=vec(x1+b,y1,0)
k2=vec(x2+b,y2,0)
k3=vec(x3,y3,0)
k4=vec(x4,y4,0)

points(pos=[k1,k2,k3,k4],radius=10.,color=color.red)
cp=curve(k1,k2,k2,k3,k3,k4,k4,k1,k3,k4,k2)

