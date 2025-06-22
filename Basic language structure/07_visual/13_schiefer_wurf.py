#13_schiefer_wurf.py
from vpython import *
h=1.2     #Abwurfhöhe
b=60.     #Breite der Bezugsebene
v0=22.5   #Anfangsgeschwindigkeit
alpha=45. #Abwurfwinkel
alpha=radians(alpha)
g=9.81
r=b/40.
h=h+r
scene.background=color.white
scene.width=600
scene.height=600
scene.center=vector(0,b/4.,0)
ball = sphere(pos=vector(-b/2.,h,0),radius=r,color=color.yellow)
box(pos=vec(0,-b/50.,0),size=vec(b,b/25.,b/2.),color=color.green)
scene.caption="\nmit Mausklick starten"
scene.waitfor('click')
dt=0.01
t=0.0
while True:
    rate(50)
    x = v0*t*cos(alpha)
    y = h + v0*t*sin(alpha) - 0.5*g*t**2
    ball.pos = vector(x-b/2.,y+r,0)
    if y<=0.0:
        break
    t=t+dt
