#L_10_02.py
print("x1 \t x2\t  y")
for x1 in False,True:
    for x2 in False, True:
        y=(x1 and not x2) or (not x1 and x2)
        print(x1,x2,y,sep="\t")
