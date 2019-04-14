import copy 
import string
import random
"""line1=input("")
line2=input("")
line3=input("")
line4=input("")
line5=input("")

line1=f.readline().splitlines()
line2=f.readline().splitlines()
line3=f.readline().splitlines()
line4=f.readline().splitlines()
line5=f.readline().splitlines()
f.close()

line1=line1.split(" ")
line2=line2.split(" ")
line3=line3.split(" ")
line4=line4.split(" ")
line5=line5.split(" ")
tableau=[line1,line2,line3,line4]"""

def Generate():
    d=[0, 2, 0, 16, 16, 2, 64, 0, 4, 512, 1024]
    c=[]
    for i in range(0,4):
        c.append([d[random.randint(0,10)],d[random.randint(0,10)],d[random.randint(0,10)],d[random.randint(0,10)]])
    
    return c
    

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def transposer(tableau):
    
    c=[[],[],[],[]]
    for i in range(0,4):
        for j in range(0,4):
            c[i].append(tableau[j][i])
    """print(c)"""
    return c

def check(tableau):
    for i in range(0,4):
        for k in range(0,4):
            if isinstance(tableau[i][k], str) :
                tableau[i][k]=int(tableau[i][k][:-10])
                

def left(tableau):
    for i in range(0,4):
        for k in range(0,4):
            for j in range(k,3):
                """print("les coordonne",i,j,k)"""
                if tableau[i][k]!=tableau[i][j+1] and tableau[i][j+1]!=0 and tableau[i][k]!=0:
                    """print("sortie", tableau)"""
                    break
                elif tableau[i][k]==tableau[i][j+1] and tableau[i][j+1]!=0:
                    
                    tableau[i][k]=str(tableau[i][k]*2)+randomString()
                    tableau[i][j+1]=0
                    """print("1",tableau)"""
                    break
                elif tableau[i][k]!=0 and tableau[i][j+1]==0:
                    """print("3",tableau)"""
                    continue
                elif tableau[i][k]==0 and tableau[i][j+1]!=0:
                    """"for z in range(0,3-k):tableau[i][3-z]=tableau[i][2-z]tableau[i][0]=0"""
                    tableau[i][k]=tableau[i][j+1]
                    tableau[i][j+1]=0
                    if(k-1>=0 and tableau[i][k-1]==tableau[i][k] ):
                        tableau[i][k-1]*=2
                        tableau[i][k]=0
                    """print("2",tableau)"""
                    break


def right(tableau):
    
    for i in range(0,4):
        for k in range(0,4):
            for j in range(k,3):
                """print("les coordonne",i,j,k)"""
                if tableau[i][3-k]!=tableau[i][2-j] and tableau[i][2-j]!=0 and tableau[i][3-k]!=0:
                    """print("sortie", tableau)"""
                    break
                elif tableau[i][3-k]==tableau[i][2-j] and tableau[i][2-j]!=0:
                    
                    tableau[i][3-k]=str(tableau[i][3-k]*2)+randomString()
                    tableau[i][2-j]=0
                    """print("1",tableau)"""
                    break
                elif tableau[i][3-k]!=0 and tableau[i][2-j]==0:
                    """print("3",tableau)"""
                    continue
                elif tableau[i][3-k]==0 and tableau[i][2-j]!=0:
                    """"for z in range(0,3-k):tableau[i][3-z]=tableau[i][2-z]tableau[i][0]=0"""
                    tableau[i][3-k]=tableau[i][2-j]
                    tableau[i][2-j]=0
                    if(4-k<=3 and tableau[i][3-k]==tableau[i][4-k]):
                        tableau[i][4-k]*=2
                        tableau[i][3-k]=0
                    """print("2",tableau)"""
                    break
                            

def up(tableau):
    d=transposer(tableau)
    left(d)
    return transposer(d)
    
def down(tableau):
    d=transposer(tableau)
    """print(d)"""
    right(d)
    """print(d)"""
    return transposer(d)

def main(move,tableau):
    d=copy.copy(tableau)
    d=[[int(k) for k in i] for i in d]
    if move=="0":
        """print("left")"""
        left(d)
    if move=="2":
        right(d)
    if move=="1":
        d=up(d)
    if move=="3":
        d=down(d)
    check(d)
    d.append([move])
    return d
d=[Generate() for k in range(0,100)]


f =open("generate.txt","w+")
for k in d:
    f.write("matrice"+"\n")
    for s in range(0,4) :
        f.write(str(k[s][0])+" "+str(k[s][1])+" "+str(k[s][2])+" "+str(k[s][3])+"\n")
    
f.close()
print(d)
w=[main(str(random.randint(0,3)),k) for k in d]
f=open("output.txt","w+")    
for k in w:
    f.write("matrice"+"\n")
    for s in range(0,4) :
        f.write(str(k[s][0])+" "+str(k[s][1])+" "+str(k[s][2])+" "+str(k[s][3])+"\n")
    f.write("moove "+str(k[4][0])+"\n")




"""for i in tableau:
    print(str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str(i[3])+" ")"""
"""print(tableau)"""
