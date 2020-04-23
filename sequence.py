seq=input("entrer la sequence \n")
print(seq)
import copy
all_sequences=[]
def create_strin(sequence):
    
    if sequence.count('?')>1:
        return create_strin(sequence[:-1])
    else :
        indexinco=sequence.index('?')
        zz=sequence.copy()
        un=sequence.copy()
        zz[indexinco]=0
        un[indexinco]=1
        all_sequences=[i+zz for i in all_sequences]+[i+un for i in all_sequences]
        