n=input()

a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0

for m in n:
    if int(m)==0:
        a+=1
    elif int(m)==1:
        b+=1
    elif int(m)==2:
        c+=1
    elif int(m)==3:
        d+=1
    elif int(m)==4:
        e+=1
    elif int(m)==5:
        f+=1
    elif int(m)==6:
        g+=1
    elif int(m)==7:
        h+=1
    elif int(m)==8:
        i+=1
    elif int(m)==9:
        j+=1
        
print("0 1 2 3 4 5 6 7 8 9")
print(f"{a} {b} {c} {d} {e} {f} {g} {h} {i} {j}")