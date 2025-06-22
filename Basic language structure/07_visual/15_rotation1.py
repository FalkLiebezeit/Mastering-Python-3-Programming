#15_rotation1.py
from vpython import *
scene.width=scene.height=600
scene.background=color.white
scene.center=vec(0,0,0)
r=1.
col=color.green
scene.range=1.5*r
rot = box(pos=vec(0,0,0),axis=vec(0,1,0),size=vec(r,r,r),color=col)
#rot =ring(pos=vec(0,0,0),axis=vec(0,0,1),radius=r,thickness=r/5.)
#rot=ellipsoid(pos=vec(0,0,0),axis=vec(1,0,0),size=vec(2.0*r,r,r))
#rot = arrow(pos=vec(0,0,0), axis=vec(r,0,0), color=col)
dt = 0.05
w=0.5    #Winkelgeschwindigkeit
while True:
    rate(25)
    rot.rotate(angle=w*dt,axis=vec(0,1,0),origin=vec(0,0,0))

