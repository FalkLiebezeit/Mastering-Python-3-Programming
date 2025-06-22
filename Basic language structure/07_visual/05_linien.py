#05_linien.py
from vpython import *
scene.width=600
scene.height=600
scene.background=color.white
r=10. #Radius der Ebene
e=sqrt(3.)*r #Kantenlänge
scene.center=vector(0,0,0)
scene.range=1.8*r
x=r*cos(pi/6.)
y=r*sin(pi/6.)
z=sqrt(6.)*e/3. #Höhe
#links unten, oben, rechts unten
v1=[(-x,-y,0),(0,r,0),(x,-y,0),(-x,-y,0)]
v2=[(-x,-y,0),(0,0,z),(0,r,0),(0,0,z),(x,-y,0)]
points(pos=v2,radius=10.,color=color.red)
c=curve(pos=v1,color=color.green)
c.append(v2,color=color.yellow)

