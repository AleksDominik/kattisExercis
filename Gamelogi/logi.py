from upemtk import *
import sys
import copy


def import_grile():
    f=open("./contrainte.txt","r")
    lines=[]
    for _ in range(2):
        line=f.readline().split('/')
        line=[k[:-1] if '\n' in k else k for k in line]
        lines.append(line)
        
        lines[-1]=[k.split('-') for k in lines[-1]]
    return lines
# print(len(import_grile(f)[0]))


class Game():
    def permuter(self,i,j):
            self.grille[i][j]=(self.grille[i][j]+1)%2
    def completable(self,cont,rangee):
        for k in range(-1,-len(rangee),-1):
            if rangee[k]==1:
                print(k)
                o=len(rangee)+k
                try:
                    index=0
                    for w in cont:
                        for l in range(w):
                            rangee[o+index]=1
                            index+=1
                        rangee[o+index]=0
                        index+=1
                    print('fini les contraintes')
                    return True
                except:
                    return False
        return True
    def complete(self,cont,rangee):
        rangee=''.join([str(k) for k in rangee])
        rangee=rangee.split('0')
        if [len(k) for k in rangee]==cont:
            return True
        else :
            return False



    def __init__(self,contraintes):
        self.grille=[[0 for _ in range(len(contraintes[0])) ] for _ in  range(len(contraintes[1]))]
        print(self.grille)
        
    def start_game(self):
        self.permuter(1,1)
        print(self.grille)
        self.permuter(1,1)
        print(self.grille)

        cree_fenetre(400,400)
        ligne(0, 200, 200, 0, couleur='black', epaisseur=1, tag='')
        while True:
            # On récupère le plus ancien événement en attente
            ev = donne_ev()
            tev = type_ev(ev)
            if ev is not None:
                print(type_ev(ev))

            if type_ev(ev) == 'Quitte':
                break
            if tev == 'Touche':
                print('Appui sur la touche', touche(ev))

            elif tev == "ClicDroit":
                print("Clic droit au point", (abscisse(ev), ordonnee(ev)))

            elif tev == "ClicGauche":
                print("Clic gauche au point", (abscisse(ev), ordonnee(ev)))

            elif tev == 'Quitte':  # on sort de la boucle
                break

            else:  # dans les autres cas, on ne fait rien
                pass

            mise_a_jour()
        def create_screen():

            pass
        

        def arreter():
            ferme_fenetre()
# if __name__=="main":
c=Game(import_grile())
c.start_game()