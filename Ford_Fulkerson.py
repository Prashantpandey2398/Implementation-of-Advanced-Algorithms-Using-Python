import copy
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
n = int(input("Enter the number of nodes : "))
#ad=[[0,10,20,0],[0,0,10,10],[0,0,0,5],[0,0,0,0]]
#ad=[[0,10,5,0],[0,0,0,10],[0,0,0,5],[0,0,0,0]]
#ad=[[0, 16, 13, 0, 0, 0],[0, 0, 10, 12, 0, 0],[0, 4, 0, 0, 14, 0],[0, 0, 9, 0, 0, 20],[0, 0, 0, 7, 0, 4],[0, 0, 0, 0, 0, 0]]
#ad=[[0, 16, 7, 0, 0, 0],[0, 0, 4, 12, 0, 0],[0, 0, 0, 0, 11, 0],[0, 0, 0, 0, 0, 19],[0, 0, 0, 7, 0, 4],[0, 0, 0, 0, 0, 0]]
ad=[[0,9,9,0,0,0],[0,0,4,8,0,0],[0,0,0,1,3,0],[0,0,0,0,0,10],[0,0,0,8,0,7],[0,0,0,0,0,0]]
#ad=[[0, 9, 3, 0, 0, 0], [0, 0, 1, 8, 0, 0], [0, 0, 0, 1, 3, 0], [0, 0, 0, 0, 0, 9], [0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0]]

print("Given adjacency matrix is : ")
for i in range(0,n):
    print(ad[i])
source_capacity=0
sink_capacity=0
for i in range(0,n):
    source_capacity+=ad[0][i]
    sink_capacity+=ad[i][n-1]

max_flow=min(source_capacity,sink_capacity)
flow=0
fd=copy.deepcopy(ad)
ffd=copy.deepcopy(ad)

while flow<max_flow:
    path=[]
    path=dfs(ad,0,n-1,path,[])
    if (n-1) in path:
        ind = path.index(n-1)
        path=path[ind:]
        path.reverse()
        flows=[]
        for i in range(0,len(path)-1):
            row=path[i]
            col=path[i+1]
            flows.append(ad[row][col])
        f=min(flows)
        flow+=f
        for i in range(0,len(path)-1):
            row=path[i]
            col=path[i+1]
            ad[row][col]-=f
            ad[col][row]+=f
    else:
        break

print("Maximum flow in this graph is :",flow)

print("Modification 1 : ")
print("Minimum values of edges to make maximum flow",flow,"should be : ")

for i in range(0,n):
    for j in range(0,n):
        if fd[i][j]>0:
            fd[i][j]-=ad[i][j]
        if fd[i][j]<0:
            fd[i][j]=0

for i in range(0,n):
    print(fd[i])

print("Modification 2 : ")
x=int(input("Enter the value of x : "))
max_flow=flow+x

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])

graph={}
for i in range(0,n):
    temp=[]
    for j in range(0,n):
        if ffd[i][j]>0:
            temp.append(str(j))
    graph[str(i)]=set(temp)

all_paths=list(dfs_paths(graph, str(0), str(n-1)))

costs=[]

for i in all_paths:
    cost=0
    for j in range(0,len(i)-1):
        row=int(i[j])
        col=int(i[j+1])
        if ad[row][col]<x:
            cost+=(x-ad[row][col])
    costs.append(cost)

#print(all_paths)
#print(costs)
#print(all_paths[costs.index(min(costs))])
i=all_paths[costs.index(min(costs))]
for j in range(0,len(i)-1):
    row=int(i[j])
    col=int(i[j+1])
    if ad[row][col]<x and ffd[row][col]>0:
        ffd[row][col]+=(x-ad[row][col])
        print("Edge from",row,"to",col,"should be increased by :",x-ad[row][col])

print("The adjacency matrix for maximum flow",max_flow,"should be : ")
for i in range(0,n):
    print(ffd[i])
