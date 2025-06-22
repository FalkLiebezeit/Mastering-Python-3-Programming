#14_ellipsenbahn.py
from vpython import *
scene.width=600
scene.height=600
b=10.     #Ellipsenhalbachse
a=1.157*b #Ellipsenhalbachse
Rm=1.0 #Radius Mond
Re=3.7*Rm #Radius Erde
rem=10.*Re #Abstand Erde Mond
scene.background=color.white
erde = sphere(pos=vector(0.1*a,0,0),radius=Re,texture=textures.earth)
mond = sphere(pos=vector(rem,0,0),radius=Rm,color=color.gray(0.8))
w=1. #Winkelgeschwindigkeit
t=0
dt=1e-3
while  True:
    rate(50)
    x = a*cos(w*t)
    y = b*sin(w*t)
    mond.pos = vector(x,y,0)
    t=t+dt
