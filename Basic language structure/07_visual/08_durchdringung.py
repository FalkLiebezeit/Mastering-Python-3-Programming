#08_durchdringung.py
from vpython import *
rc=10.    #Radius des Kegels
hc=3.*rc  #Höhe des Kegels
scene.background=color.white
scene.width=600
scene.hight=600
scene.range=2.1*rc
rz=rc/2.  #Radius des Zylinders
lz=2.5*rc #Länge des Zylinders
z=rc/1.5  #Verschiebung des Zylinders
cone(pos=vec(0,-hc/2.5,0),axis=vec(0,hc,0),radius=rc)
cylinder(pos=vec(-lz/2.,0,z),axis=vec(lz,0,0),radius=rz)
