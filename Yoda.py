c=input("")
d=input("")
c=[i for i in c]
d=[j for j in d]
"""print(c,d)"""


if(len(c)>len(d)):
    """print("c>d")"""
    for ee in range(0,len(d)):
        if(c[-ee-1]>d[-ee-1]):
            d[-ee-1]=" "          
        elif c[-ee-1]==d[-ee-1] :
            continue

        else :
            c[-ee-1]=" "

else :
    """print("egalite")"""
    for ee in range(0,len(c)):
        """print(d[-ee-1],c[-ee-1])"""
        if(c[-ee-1]>d[-ee-1]):
            d[-ee-1]=" "
        elif c[-ee-1]==d[-ee-1] :
            1+1
            """print("egalite des termes",d[-ee-1])"""
        elif(c[-ee-1]<d[-ee-1]) :
            """print("dfdf")"""
            c[-ee-1]=" "

Boolc=False
Boold=False
k=""
kk=""
for i in c:
    if i!=" ":
        Boolc=True
for sss in d:
    if sss!=" ":
        Boold=True

if(Boolc):
    for i in c:
        if(i!=" "):
            k+=i
    k=int(k)
if(Boolc!=True) :
    k="YODA"
if(Boold):
    for j in d:
        if(j!=" "):
            kk+=j
    kk=int(kk)
if(Boold !=True):
    kk="YODA"

print(k)
print(kk)