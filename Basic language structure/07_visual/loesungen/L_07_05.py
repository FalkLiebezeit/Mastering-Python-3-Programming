#L07_05.py
from vpython import *
scene.width=600
scene.height=600
scene.background=color.white

Rs=10
Re=2
Rm=1
re=40.0 
rm=1.5*re+Rm
scene.range=1.8*re
sphere(pos=vec(0,0,0),radius=Rs,color=color.yellow)
erde=sphere(pos=vec(re,0,0),radius=Re,color=color.blue)
mond=sphere(pos=vec(rm,0,0),radius=Rm,color=color.green)
dt = 0.005
we=1
wm=12*we
while True:
    rate(50)    
    rx=erde.pos.x
    ry=erde.pos.y
    erde.rotate(angle=we*dt,axis=vec(0,0,1),origin=vec(0,0,0))
    mond.rotate(angle=(we+wm)*dt,axis=vec(0,0,1),origin=vec(rx,ry,0))


