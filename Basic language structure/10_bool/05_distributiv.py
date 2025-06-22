#05_distributiv.py
print("x1  x2 \t y1 \t y2 \t y3 \t y4",sep='\t')
for x1 in False, True:
    for x2 in False, True:
        for x3 in False, True:
            y1=(x1 and x2) or (x1 and x3)
            y2=x1 and (x2 or x3)
            y3=(x1 or x2) and (x1 or x3)
            y4=x1 or (x2 and x3)
            print(x1,x2,y1,y2,y3,y4,sep='\t')