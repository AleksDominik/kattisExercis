m=input(" ")
c=[]
for i in range(0,int(m)):
    k=input(" ")
    c.append(k)


c=[w+"^" for w in c]

d=[str(element)for element in c]
nombredepuissance=[element.split("^") for element in d]
hauteurdelatour=[len(f) for f in nombredepuissance]

d=max(hauteurdelatour)
print(d)
for i in 
print(nombredepuissance)
"""c=[int(element) for element in c]
c.sort() 
print(c)"""