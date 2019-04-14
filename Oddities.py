x=int(input(""))
c=[]
for i in range(0,x):
    c.append(int(input("")))
for w in c :
    if w%2==0: 
        print(str(w)+" is even")
    else:
        print(str(w)+" is odd")