#04_punkte.py
from vpython import *
scene.width=600
scene.height=600
scene.background=color.white
e=1.
scene.center=vector(e/2,e/2,e/2)
scene.range=1.2*e
v=[(0,0,0),(0,0,e),(0,e,0),(0,e,e),
    (e,0,0),(e,0,e),(e,e,0),(e,e,e),(e/2,e/2,e/2)]
box(pos=vector(e/2,e/2,e/2),size=vector(e,e,e),
    axis=vector(1,0,0),opacity=0.5)
points(pos=v,color=color.red)

