n = int(input("Enter the number of nodes : "))
graph = {}
for i in range(0,n):
    j = input("Enter the edges flowing from the node : ")
    temp=j.split(",")
    graph[str(i)]=temp

matrix = [[0 for x in range(n)] for y in range(n)] 

#print(graph)

for i in graph.keys():
    j = graph.get(i)
    for k in j:
        if k is not '':
            matrix[int(i)][int(k)]=1
print(matrix)

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

source_capacity=0
sink_capacity=0
for i in range(0,n):
    source_capacity+=matrix[0][i]
    sink_capacity+=matrix[i][n-1]

max_flow=min(source_capacity,sink_capacity)
flow=0
disjoint_paths=[]

while flow<max_flow:
    path=[]
    path=dfs(matrix,0,n-1,path,[])
    if (n-1) in path:
        ind = path.index(n-1)
        path=path[ind:]
        path.reverse()
        disjoint_paths.append(path)
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

print("Maximum number of edge-disjoint paths are :",flow)
print("Disjoint Paths are : ")
for i in disjoint_paths:
    print(i)
