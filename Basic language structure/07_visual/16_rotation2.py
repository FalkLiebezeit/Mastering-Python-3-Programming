#16_rotation2.py
from vpython import *
scene.width=scene.height=600
scene.background=color.white
R=5.0  #Radius der Sonne
r=10.0 #Abstand Sonne Merkur
sphere(pos=vec(0,0,0),axis=vec(1,0,0),radius=R,color=color.yellow)
merkur=sphere(pos=vec(r,0,0),axis=vec(1,0,0),radius=0.2*R,color=color.red)
venus=sphere(pos=vec(2*r,0,0),axis=vec(1,0,0),radius=0.3*R,color=color.green)
erde=sphere(pos=vec(3*r,0,0),axis=vec(1,0,0),radius=0.5*R,texture=textures.earth)
dt = 0.05
w1=0.3
w2=0.2
w3=0.1 #Winkelgeschwindigkeit
while True:
    rate(25)
    merkur.rotate(angle=w1*dt,axis=vec(0,1,0),origin=vec(0,0,0))
    venus.rotate(angle=w2*dt,axis=vec(0,1,0),origin=vec(0,0,0))
    erde.rotate(angle=w3*dt,axis=vec(0,1,0),origin=vec(0,0,0))

