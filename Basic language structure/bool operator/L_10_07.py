#L_10_07.py
print("Nr.\tD\tC\tB\tA\ta\tb\tc\td\te\tf\tg")
dezimal=-1
for D in 0,1:
    for C in 0, 1:
        for B in 0, 1:
            for A in 0, 1:
                dezimal=dezimal+1
                a =  D | (A & C) | (B & ~C) | (~A & ~C)
                b =  D | ~C | (A & B) | (~A & ~B)
                c =  A | C | D | ~B
                d =  D | (B & ~A) | (B & ~C) | (~A & ~C) | (A & C & ~B)
                e =  ~A & (B | ~C) & (~B | ~D)
                f =  D | (C & ~A) | (C & ~B) | (~A & ~B)
                g =  D | (B & ~A) | (B & ~C) | (C & ~B)
                if (a or b or c or d or e or f)==-1:
                    a=b=c=d=e=f=1
                else:
                    a=b=c=d=e=f=0
                print(dezimal,D,C,B,A,a,b,c,d,e,f,g,sep="\t")