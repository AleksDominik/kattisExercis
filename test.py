table={0,0,0,1,1,1,0,1,1,1,1,1}

# Find the max length of the consecutive 1nsa[] = {0,0,0,1,1,1,0,1,1,1,1,1}

# Find the max length of the consecutive 1n

table=list([0,0,0,1,1,1,0,1,1,1,1,1])

print(table)
records=[]
for k in range(len(table)):
    if (table[k]==1) and (k<len(table)-2):
        # print(k)
        ind=1
        nextt=1
        
        while (k+nextt<=len(table)-1) and (table[k+nextt]==1) :
            nextt+=1
            ind+=1
        records.append(ind)
print(max(records))
    
    
    