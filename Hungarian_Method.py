# Hunagarian Method
import copy
import time
start_time = time.clock()

def dfs(a,current,dest,path,f):
    if current==dest:
        path.append(current)
    else:
        path.append(current)
        temp=a[current]
        j=-1
        for i in temp:
            j+=1
            if i>0 and (j not in path) and (dest not in path):
                dfs(a,j,dest,path,f)
    f.append(current)
    return f    

def bipartite_matching(l,matrix1):
    source_capacity=0
    sink_capacity=0
    n=2*l+2
    matrix=[[0 for x in range(n)] for y in range(n)]
    matrix2=copy.deepcopy(matrix1)
    for i in range(0,l):
        matrix[0][i+1]=1
        matrix[l+i+1][n-1]=1
    
    for i in range(0,l):
        for j in range(0,l):
            matrix[i+1][l+j+1]=matrix1[i][j]
    
    for i in range(0,n):
        source_capacity+=matrix[0][i]
        sink_capacity+=matrix[i][n-1]
    
    max_flow=min(source_capacity,sink_capacity)
    flow=0
    while flow<max_flow:
        path=[]
        path=dfs(matrix,0,n-1,path,[])
        if (n-1) in path:
            ind = path.index(n-1)
            path=path[ind:]
            path.reverse()
            flows=[]
            for i in range(0,len(path)-1):
                row=path[i]
                col=path[i+1]
                flows.append(matrix[row][col])
            f=min(flows)
            flow+=f
            for i in range(0,len(path)-1):
                row=path[i]
                col=path[i+1]
                matrix[row][col]-=f
                matrix[col][row]+=f
        else:
            break

    matchings=[]    
    for i in range(0,l):
        for j in range(0,l):
            matrix2[i][j]-=matrix[i+1][l+1+j]
    for i in range(0,l):
        temp=matrix2[i]
        temp1=[]
        if 1 in temp:
            j = temp.index(1)
            temp1.append(i)
            temp1.append(j)
            matchings.append(temp1)
    return matchings

n = int(input("Enter the number of nodes : "))
#ad=[[250,400,350],[400,600,350],[200,400,250]]
#ad=[[1,4,5],[5,7,6],[5,8,8]]
ad=[[90,75,75,80],[35,85,55,65],[125,95,90,105],[45,110,95,115]]
#ad=[]

'''for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(int(input("Enter the cost : ")))
    ad.append(temp) '''
fd = copy.deepcopy(ad)

for i in range(0,n):
    temp=ad[i]
    s=min(temp)
    ad[i]=[ad[i][j]-s for j in range(n)]

temp=[]
for i in range(0,n):
    s=ad[0][i]
    for j in range(0,n):
        if s>ad[j][i]:
            s=ad[j][i]
    temp.append(s)

for i in range(0,n):
    for j in range(0,n):
        ad[j][i]-=temp[i]

ffd=[[0 for x in range(n)] for y in range(n)]

for i in range(0,n):
    for j in range(0,n):
        if ad[i][j]==0:
            ffd[i][j]=1

fad=copy.deepcopy(ffd)
matchings=bipartite_matching(n,ffd)

while len(matchings)<n:
    source_set=[]
    target_set=[]
    fadt=[[fad[x][y] for x in range(n)] for y in range(n)]
    rrac=[0 for i in range(0,2*n)]  #count of zeros in rows and columns
    for i in range(0,n):
        count1,count2=0,0
        for j in range(0,n):
            if fad[i][j]==1:
                count1+=1
            if fadt[i][j]==1:
                count2+=1
        rrac[i]=count1
        rrac[i+n]=count2
    rac=copy.deepcopy(rrac)#updated count of zeros in rows and columns
    while max(rac)>0:
        pn=[]
        for i in range(0,2*n):
            if rac[i] == max(rac):
                pn.append(i)        
        max_pn=rrac[pn[0]]
        index=pn[0]
        for i in pn:
            if max_pn<rrac[i]:
                max_pn=rrac[i]
                index=i
        if index>=n:
            for i in range(0,n):
                if rac[i]>0:
                    if fad[i][index%n]==1:
                        rac[i]-=1            
            target_set.append(index%n)
        else:
            for i in range(n,2*n):
                if rac[i]>0:
                    if fad[index][i-n]==1:
                        rac[i]-=1
            source_set.append(index)
        rac[index]-= max(rac)
    temp=[]
    for i in range(0,n):
        for j in range(0,n):
            if (i not in source_set) and (j not in target_set):
                temp.append(ad[i][j])
    minimum=min(temp)
    for i in range(0,n):
        for j in range(0,n):
            if (i not in source_set) and (j not in target_set):
                ad[i][j]-=minimum
            elif (i in source_set) and (j in target_set):
                ad[i][j]+=minimum
                
    ffd=[[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if ad[i][j]==0:
                ffd[i][j]=1
    fad=copy.deepcopy(ffd)
    matchings=bipartite_matching(n,ffd)

print("The tasks should be allocated in the following manner : ")
for i in range(0,len(matchings)):
    print("Person",i+1,"shold be allocated task",matchings[i][1]+1)

cost=0
for i in range(0,len(matchings)):
    row=matchings[i][0]
    col=matchings[i][1]
    cost+=fd[row][col]

print("The minimum cost required to complete all the tasks is : ",cost)
print("Time taken to execute the entire program is : ",time.clock()-start_time)
