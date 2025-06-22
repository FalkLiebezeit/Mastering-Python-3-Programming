#04_demorgan.py
print("x1 \t x2 \t y1 \t y2 \t y3 \t y4")
for x1 in False, True:
    for x2 in False, True:
        y1=not(x1 and x2)
        y2=not x1 or not x2
        y3=not(x1 or x2)
        y4=not x1 and not x2
        print(x1,x2,y1,y2,y3,y4,sep='\t')