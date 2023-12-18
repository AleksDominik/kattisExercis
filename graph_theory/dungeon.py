## Solution proposition for dungeon problem
#https://open.kattis.com/problems/dungeon


import sys

def read_dungeon():
    line=sys.stdin.readline()
    # print('first line is ', line)
    if line=='0 0 0\n':
        return -1
    else:
        L,R,C=[int(k.replace('\r','')) for k in line.split(' ')]
        g=[]
        for h in range(L):
            g.append([])
            for _ in range(R):
                l=sys.stdin.readline()
                l=l.replace('\n','')
                l=[k for k in l]
                g[-1].append(l)
            sys.stdin.readline()                
        return g,L,R,C

def solve (g, L,R, C):

    prev=[   [ [None for _ in range(C) ] for __ in range(R)  ]    for h in range(L)]
    visited=[   [ [False for _ in range(C) ] for __ in range(R)  ]    for h in range(L)]
    # print('>>>prev', prev)

    dh=[0,0,0,0, 1,-1]
    dr=[-1,1,0,0,0,0]
    dc=[0,0,1,-1,0,0]
    q=[]
    for k in range(L):
        for r in range(R):
            for c in range(C):
                if g[k][r][c]=='S':
                    S=[k,r,c]
                    # print(S)
                elif g[k][r][c]=='E':
                    E=[k,r,c]
                    # print(E)
    # print(">>>E",E)
    hs,rs,cs=S
    visited[hs][rs][cs]=True
    q.append(S)



    while q!=[]:
        # print("looping")
        # print(">>>>q",q)
        node=q.pop(0)
        for k in range(len(dr)):
            h=node[0]+dh[k]
            r=node[1]+dr[k]
            c=node[2]+dc[k]
            if h>=0 and h<L and r>=0 and r<R and c>=0 and c<C:
                if g[h][r][c]!="#" and visited[h][r][c]==False :
                    q.append([h,r,c])
                    visited[h][r][c]=True
                    prev[h][r][c]=node
    path=reconstruct(S, E, prev)
    # print('>>>prev', prev)

    return prev ,path

def reconstruct(s, e, prev):
    path=[]
    at=e
    while at!=None:
        path.append(at)
        h,r,c=at
        at=prev[h][r][c]
    path=path[::-1]
    if path[0]!=s:
        return []

    return path

    # q.append(s)
    # visited[s]=True
    # prev=[None for _ in range(n)]
    # for k in range(len(dr)):
    #     rr=r

if __name__=='__main__':

    data= read_dungeon()
    while data!=-1:  
        # if not data :
        #     return -1
        g,L,R,C= data
        prev,path=solve( g, L, R, C)
        if len(path)==0:
            print('Trapped!')
        else:
            print(f'Escaped in {len(path)-1} minute(s).')
        # print(">>>sol",len(path))
        data= read_dungeon()
