#09_verbindung.py
from vpython import *
scene.background=color.white
scene.width=scene.height=600
a=5.
b=10.
scene.range=1.5*b
scene.autocenter=True
p1=pyramid(pos=vec(0,a,0),axis=vec(0,1,0),size=vec(a,a,a),color=color.green)
q1=box(pos=vector(0, a/2,0),size=vector(a,a,a),color=color.red)
q2=box(pos=vector(0,-b/2,0),size=vector(b,b,b),color=color.blue)
werkstueck=compound([p1,q1,q2])

