#17_zufaellig.py
from vpython import *
a=10.
r=a/20.
scene.background=color.white
scene.width=scene.height=600
scene.center=vector(0,0,0)
scene.range=a
teil = sphere(radius=r,color=color.red)
teil.pos=vector(0,0,0)
attach_trail(teil,radius=0.05,color=color.blue)
i=0
while i<10:
    sleep(0.8)
    alpha = pi*random()
    phi = 2.0*pi*random()
    x = a*sin(alpha)*cos(phi)
    y = a*sin(alpha)*sin(phi)                                          
    teil.pos=vector(x,y,0)
    i=i+1
