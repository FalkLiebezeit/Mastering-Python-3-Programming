#03_negation.py
print("x1\t x2\t NAND \t NOR")
for x1 in False,True:
    for x2 in False,True:
        y1=not (x1 & x2)
        y2=not (x1 | x2)
        print(x1,x2,y1,y2,sep='\t')