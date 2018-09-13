l = int(input("Enter the number of nodes on the left-side : "))
r = int(input("Enter the number of nodes on the right-side : "))
graph = {}
for i in range(1,l+1):
    j = input("Enter the edges flowing from the left-node to right-node : ")
    temp=j.split(",")
    graph[str(i)]=temp

n = 2+l+r
matrix = [[0 for x in range(n)] for y in range(n)] 

for i in range(0,l):
    matrix[0][i+1]=1

for i in range(0,r):
    matrix[l+i+1][n-1]=1

#print(graph)

for i in graph.keys():
    j = graph.get(i)
    for k in j:
        if k is not '':
            matrix[int(i)][l+int(k)]=1

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

matchings=[]
print("Maximum number of matching are :",flow)
for i in disjoint_paths:
    matchings.append(i[1:len(i)-1])

print("Matchings are : ")
for i in matchings:
    print("Left Node is : ",i[0], "and Right node is : ",i[1]-l)
