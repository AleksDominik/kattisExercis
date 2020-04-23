class Solution(object):
    def numOffices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # your code here
        row_len=(len(grid))
        col_len= len(grid[0])
        al_readyve=[["0"]*col_len]*row_len
        def get_neighbour(indices):
            toreturn=[]
            if indices[0]<row_len-1:
                toreturn.append([indices[0]+1,indices[1]])
            if indices[1]<col_len-1:
                toreturn.append([indices[0],indices[1]+1])
            if indices[0]>0:
                toreturn.append([indices[0]-1, indices[1]])
            if indices[1]>0:
                toreturn.append([indices[0], indices[1]-1])
            return toreturn
        def check(i,j,old):
            #check if i,j point is in old neighbour
            print(old)
        
            for k in old:
                if str(i)+str(j) in k.split('*'):
                    return False
                else: 
                    return True
        
        all_n=[]
        b=True
        for i in range(row_len):
            for j in range(col_len):
                if(grid[i][j]=='1'):
                    print('dfdjfdf')
                    if b:
                        print('initialisation',all_n)
                        all_n=[str(i)+'*'+str(j)]
                        print(all_n)
                        b=False
                    neighb=get_neighbour([i,j])
                    for k in neighb:
                        for ww in all_n:
                            if grid[k[0]][k[1]]=='0' or not check(k[0],k[1],ww.split("/")):
                                pass 
                            else:
                                all_n=[ss for ss in all_n if ss!=ww].append(ww+'/'+str(k[0])+'*'+str(k[1]))







        
        return 0

def get_matrix():
    row = int(input())
    col = int(input())
    grid = [["0"]*col]*row

    for i in range(row):
        line = input()
        grid[i] = list(line)[0:col]
    return grid

        
if __name__ == "__main__":
    sol = Solution()
    matrix = get_matrix()
    offices = sol.numOffices(matrix)
    print(offices)











Second exercice solution

    def minimumConcat(initial, goal):
   #Put your code here
   

   list_sub=[initial[i: j] for i in range(len(initial)) for j in range(i + 1, len(initial) + 1)] 
   def find_first(strr,list_sub,ind,lenn):
       #print('ddfd',strr)
       maxx=-9999
       toreturn=[]
       if ind==lenn:
           return strr
       for i in range(ind,len(strr)):
           if strr[ind:i] in list_sub and i>=maxx:
                maxx=i
       if maxx==-9999:
           return strr
       if ind==0 and maxx!=-9999:
           toreturn.append(strr[:maxx])
      # print(strr)
       toreturn.append(find_first(strr[maxx:],list_sub,maxx,lenn))
       #print(toreturn)
       return toreturn








 Last Exercice

       You are again the owner of a coworking space like WeWork and your office building is rectangular. You team just created many wall partitions to create mini offices for startups. Your office campus is represented by a 2D array of 1s (floor spaces) and 0s (walls). Each point on this array is a one foot by one foot square. Before renting to tenants, you want to reserve an office for yourself. You wish to fit the largest possible rectangular table in your office, and you will select the office that fits this table. The table sides will always be parallel to the boundaries of the office building. What is the area of the biggest table that can fit in your office?



Functions

biggestTable() has one parameter:

grid: a 2D grid/array of 1s and 0s


Input Format

For some of our templates, we have handled parsing for you. If we do not provide you a parsing function, you will need to parse the input directly. In this problem, our input format is as follows:

The first line is the number of rows in the 2D array
The second line is the number of columns in the 2D array
The rest of the input contains the data to be processed

Here is an example of the raw input:

4
5
11110
11010
11000
00000



Expected Output

Return the area of the biggest right-angled parallelogram made of 1s in the grid. Assume the grid is surrounded by 0s (walls).



Constraints
Assume that the bounds of the array are the following:
The total amount of elements in the array: width x height <= 10^6


Example

Example biggestTable() Input

grid: 
	[[1, 0, 1, 1, 1],
	 [1, 0, 1, 1, 1],
	 [1, 1, 1, 1, 1],
	 [1, 0, 0, 1, 0]]


Example Output

9


Solution

The top right of the grid consists of a rectangle with nine 1s in it, the biggest possible space for our table.
