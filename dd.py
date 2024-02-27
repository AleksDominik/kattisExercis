from typing import List
def is_ananagram(word1: str,word2: str)->bool:
    return sorted( word1.lower())==sorted(word2.lower())

def solve(dns_entries: List[str]) -> str:
    dns_type=['A', 'AAAA','CNAME']
    lines=[]
    hosts={}
    for line in dns_entries:
        for tdns in dns_type:
            if tdns in line:
                idtype= line.index(tdns)
                host=line[idtype+1:-1].strip()
                if host in hosts:
                    hosts[host].append(tdns)
                else:
                    hosts[host]=[tdns]
                break
    ranked=[]
    for h in hosts:
        ranked.append( (h,len( hosts[h] )) )
    ranked=sorted(ranked, key= lambda x:x[1])  
    ranked=[f'{k} - {h}' for k,h in ranked]
    return ranked



d=solve([
            "b.x.example.     A     192.168.0.1",
            "a.x.example.     AAAA  2001:db8::1",
        ])
print(d)