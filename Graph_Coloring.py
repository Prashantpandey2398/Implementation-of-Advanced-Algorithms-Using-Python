#n=5
#a=[[0,1,0,0,0],[1,0,1,1,1],[0,1,0,1,0],[0,1,1,0,1],[0,1,0,1,0]]
#n=4
#a=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#n=4
#a=[[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]

import time
n = int(input("Enter the number of nodes : "))
graph = {}
for i in range(0,n):
    print("Enter the edges flowing from the node",i,":",end=" ")
    j = input("")
    temp=j.split(",")
    graph[str(i)]=temp

a = [[0 for x in range(n)] for y in range(n)] 

for i in graph.keys():
    j = graph.get(i)
    for k in j:
        if k is not '':
            a[int(i)][int(k)]=1
            a[int(k)][int(i)]=1
print("Given adjacency matrix is : ")
print(a)

start_time = time.clock()
                
def check(a,i,n,count,sol,j):
    check_sol=a[count]
    check_sol1=[]
    for k in range(0,count+1):
        if check_sol[k]==1:
            check_sol1.append(sol[k])
    if j not in check_sol1:
        return 1

def color(a,i,n,count,sol):
    if count==n:
        return 1
    for j in range(1,i+1):
        if check(a,i,n,count,sol,j):
            sol[count]=j
            b=color(a,i,n,count+1,sol)
            if b==1:
                return 1

for i in range(1,n+1):
    x=0
    count=0
    sol=[0 for j in range(0,n)]
    x=color(a,i,n,count,sol)
    if x==1:
        break

print("The minimum number of colors required to color entire graph i.e.(Chromatic number) is :",i)
print("The colors on the nodes of the graph are :",sol)
print("Time taken by the algorithm is :",time.clock()-start_time)
