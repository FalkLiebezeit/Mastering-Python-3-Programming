#11_zylinder_waagerecht.py
from vpython import *
scene.background=color.white
scene.width=600
scene.height=300
l=10.   #Laenge der Spule
r=l/5.  #Radius des kerns
scene.center=vector(0,0,0)
cs=vector(1,0.7,0.2)   #kupferfarben
helix(pos=vec(-l/2,0,0),axis=vec(l,0,0),radius=1.25*r,coils=10,thickness=0.3,color=cs)
np = cylinder(pos=vec(l/2,0,0), axis=vec(l/2,0,0),radius=r, color=color.red)
sp = cylinder(pos=vec(0,0,0), axis=vec(l/2,0,0),radius=r, color=color.green)
magnet=compound([np,sp])
magnet.pos=vector(0,0,0)
dx = 0.1
while True:
    rate(50) 
    x = magnet.pos           
    x = x+vector(dx,0,0)                                             
    magnet.pos = x                                                          
    if x.x>l/4. or x.x<=-l/4.:
        dx = -dx
