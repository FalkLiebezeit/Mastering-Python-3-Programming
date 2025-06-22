#07_kugeln2.py
from vpython import *
scene.background=color.white
scene.width=600
scene.height=600
e = 5   #Gitterabstand
R = 0.5 #Radius eines Atomrumpfes
for x in range(-e,e):
    for y in range(-e,e):
        for z in range(-e,e):
            sphere(pos=vector(x,y,z),radius=R,color=color.red)
