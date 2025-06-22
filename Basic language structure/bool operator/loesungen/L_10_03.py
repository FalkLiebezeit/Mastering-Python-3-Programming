#L_10_03.py
print("x1 \t x2\t x3\t x4\t y1\t y2")
for x1 in False,True:
    for x2 in False, True:
        for x3 in False, True:
            for x4 in False, True:
                y1=( not x1 or x2 or x3) and not (x1 or x4)
                y2= not x1 and  not x4 
                print(x1,x2,x3,x4,y1,y2,sep="\t")