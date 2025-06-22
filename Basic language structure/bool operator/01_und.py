#01_und1.py
print("x1\tx2\ty")
for x1 in False,True:
    for x2 in False,True:
        y=x1 and x2
        #y=x1 & x2
        print(x1,x2,y,sep='\t')