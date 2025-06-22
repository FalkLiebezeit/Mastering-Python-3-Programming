#12_ball_wand.py
from vpython import *
scene.width=scene.height=600
scene.background=color.white
cw=color.gray(0.9) #Farbe der Wände
b = 5.0 #Breite
d = 0.3 #Dicke der Wand
r=0.4   #Ballradius
s2 = 2*b - d
s3 = 2*b + d
#Wand rechts
box (pos=vec(b, 0, 0), size=vec(d, s2, s3), color = cw)
#Wand links
box (pos=vec(-b, 0, 0), size=vec(d, s2, s3), color = cw)
#Wand unten
box (pos=vec(0, -b, 0), size=vec(s3, d, s3), color = cw)
#Wand oben
box (pos=vec(0, b, 0), size=vec(s3, d, s3), color = cw)
#Wand hinten
box(pos=vec(0, 0, -b), size=vec(s2, s2, d), color = cw)
ball = sphere(radius=r,color=color.yellow)
ball.m = 2.0   #Masse des Balls
ball.p = vec(-0.15, -0.23, 0.27) #Impuls
#ball.p = vec(0,-1,0)
#ball.p = vec(-1,0,0)
#ball.p = vec(0,-1,-1)
b = b - d*0.5 - ball.radius
dt = 0.2
while True:
    rate(100)
    ball.pos = ball.pos + (ball.p/ball.m)*dt
    if not (b > ball.pos.x > -b):
        ball.p.x = -ball.p.x
    if not (b > ball.pos.y > -b):
        ball.p.y = -ball.p.y
    if not (b > ball.pos.z > -b):
        ball.p.z = -ball.p.z
    

