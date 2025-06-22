#L_07_04.py
#Oktaeder
from vpython import *
scene.background=color.white
scene.width=scene.height=600
a=5.
b=10.
scene.range=1.5*b
scene.autocenter=True
p1=pyramid(pos=vec(0,a,0),axis=vec(0,1,0),size=vec(a,a,a),color=color.blue)
p2=pyramid(pos=vec(0,a,0),axis=vec(0,-1,0),size=vec(a,a,a),color=color.red)
oktaeder=compound([p1,p2])


