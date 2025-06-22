#20_ereignisverarbeitung.py
from vpython import *
scene.title="<h2>Rotierender Spannungs- und Leistungszeiger</h2>"
scene.width=scene.height=600
scene.background=color.white

laeuft = True
col=color.yellow

def start(b):
    global laeuft
    laeuft = not laeuft
    if laeuft: b.text = "Pause"
    else: b.text = "Start"
    
def omega(s):
    txtA.text = "{:1.2f}".format(s.value)

def sichtbar(b):
    if b.checked:
        p.visible = True
    else:
        p.visible = False

u_s=2.
p_s=1.5
d=0.025
scene.range = 1.2*u_s
u=arrow(pos=vec(0,0,0),axis=vec(0,u_s,0),color=color.blue)
p=arrow(pos=vec(0,0,0),axis=vec(p_s,0,0),color=col)
p.visible=False
u.shaftwidth=d
p.shaftwidth=d
button(text="Pause",pos=scene.title_anchor,bind=start)
scene.append_to_caption("\n\n")
scene.caption="\n  Frequenz ändern:\n\n"
sldF=slider(min=0,max=6.28,value=1,length=300,bind=omega,right=4)
txtA=wtext(text="{:1.2f}".format(sldF.value))
scene.append_to_caption(" rad/s\n\n")
checkbox(bind=sichtbar, text="Leistungszeiger anzeigen\n\n")
dt=0.01
w=1.
while True:
    rate(1/dt)
    if laeuft:
        w=sldF.value
        u.rotate(angle=w*dt,axis=vec(0,0,1))
        p.rotate(angle=2.0*w*dt,axis=vec(0,0,1))