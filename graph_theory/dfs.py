#death first algorithm
#suppose we begin with a very simple graph
# A=> B,C
# B=>D,C
#C=>E,F,G
#G=>F

#firstly read input and create a adjacency list
import sys
import random

def input_graph():
    n=sys.stdin.readline()
    print(n)
    n=int(n)
    g=[[] for _ in range(n)]
    visited=[False for _ in range(n)]
    
    for k in range(n):
        print('new node')
        sys.stdout.write(f'list the index of all node connected to the the node {k} separated by <,>')
        inp=sys.stdin.readline()
        try:
            for l in inp.split(','):
                g[k].append(int(l.replace('\n','')))
        except Exception as m:
            print(m)
    return n,g,visited


def generate_graph(j=5):
    n=random.randint(0,j)
    g=[]
    visited=[False for _ in range(n)]
    for k in range(n):
        g.append(random.sample(range(n), random.randint(0,n)))
    print(g)
    return n,g,visited


#n,g,visited=input_graph()  
n,g,visited=generate_graph(20)        
    
    
print(g)
def dfs(at):
    print('I am visiting node ', at, visited)
    
    if visited[at]:
        return -1
    visited[at]=True
    neighbours=g[at]
    for next in neighbours:
        dfs(next)

component=[0 for _ in range(n)]

def findComponent():
    count=0
    for k in range(n):
        if not visited[k]:
            count+=1
            print(count)
            dfs_component(k,count)
    return  (count,component)
        
    
def dfs_component(at,count):
    visited[at]=True
    component[at]=count
    print(component)
    neighbours=g[at]
    for next_ in neighbours:
        if not visited[next_]:
            dfs_component(next_,count)

def solve(s):
    q=[]
    q.append(s)
    visited[s]=True
    prev=[None for _ in range(n)]
    while q!=[]:
        print('the queue is',q)
        node=q.pop(0)
        neighbours=g[node]
        for nxt in neighbours:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt]=True
                prev[nxt]=node
    return prev
def reconstruct(s,e,prev):
    print('the prev is ',prev)
    path=[]
    at=e
    while at!=None:
        path.append(at)
        at=prev[at]
        
    path=path[::-1]
    print('the path is ',path)
    if  path[0]==s:
        return path
    return []

def breath_first(s,e):
    prev=solve(s)
    return reconstruct(s,e,prev)

def top_sort():
    #take a random node do a dfs and add backward evry node in a backtrack step of dfs

    
start_node=0
#dfs(start_node)
count=0
#print(findComponent())
print(breath_first(0,4))


#x= 
#g=['A','B','C','D','E','F','G']
#n=len(g)
