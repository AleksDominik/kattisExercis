"""
solution of a problem 4 thoughs
https://open.kattis.com/problems/4thought



"""



import sys
import functools
import itertools
import operator
n=int(sys.stdin.readline())
c=[int(sys.stdin.readline()) for f in range(n) ]
# print('c is ')
# print(c)

operators=['+','-','*','/']
op=[operator.add, operator.sub,operator.mul, operator.floordiv]
op_dic=dict(zip(operators,op))
# print(len(op))

#print(list(itertools.permutations(operators,3)))
space=[[a,b,c]for a in operators for b in operators for c in operators]


class thoughtfour():


    def __init__(self) -> None:
        self.search()
    # print(len(space))
    def compute (self,permu,table):
        # print(permu, table)
        
        try: 
            if '/' in permu:
                ind=permu.index('/')
                res=table[ind]//table[ind+1]
                if ind+1>=len(permu):
                    table=table[:ind]+[res]
                else:
                    table=table[:ind]+[res]+table[ind+2:]
                permu.pop(ind)
                # print('/ reached')
                # print(permu, table)
                permu, table = self.compute(permu, table)

            if '*' in permu:
                ind=permu.index('*')
                res=table[ind]*table[ind+1]
                if ind+1>=len(permu):
                    table=table[:ind]+[res]
                else:
                    table=table[:ind]+[res]+table[ind+2:]
                permu.pop(ind)
                # print('* reached')
                # print(permu, table)
                permu, table = self.compute(permu, table)
            
            if '+'  in permu or '-' in permu:
                indp=permu.index('+')if '+' in permu else 100000000
                indm=permu.index('-') if '-' in permu else 100000000
                ind = min([indp, indm])
                # print(ind)
                res= op_dic[permu[ind]](   table[ind],table[ind+1])
                if ind+1>=len(permu):
                    table=table[:ind]+[res]
                else:
                    table=table[:ind]+[res]+table[ind+2:]
                permu.pop(ind)
                # print('+ reached')
                # print(permu, table)
                permu, table = self.compute(permu, table)
            
            return permu,table


        except Exception as E :
            
            print(E)
            print('not find')
            pass
        # print('nothing')
        # print(permu, table)
        return -1



    def search(self):
        self.all_poss=[]
        self.all_poss_per=[]
        for perm in space:
            self.all_poss_per.append(perm.copy())
            _, test=self.compute(perm, [4,4,4,4])
            # print(test[0], result)
            self.all_poss.append(test[0])
        # print(self.all_poss)
        # print(self.all_poss_per)
    def check(self,result):
        if result in self.all_poss:
            # print('result trouvé')
            t=self.all_poss_per[self.all_poss.index(result)]
            print('4 '+t[0]+' 4 '+t[1]+' 4 '+t[2]+' 4 = '+str(result))
            # print(t)
            return -1
        print('no solution')
        return False

if __name__=='__main__':
    t=thoughtfour()
    for res in c:
        t.check(res)