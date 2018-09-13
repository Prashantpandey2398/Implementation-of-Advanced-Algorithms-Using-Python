from scipy.optimize import linprog
import copy

n = int(input("Enter the number of nodes : "))
graph = {}
for i in range(0,n):
    j = input("Enter the edges flowing from the node : ")
    temp=j.split(",")
    graph[str(i)]=temp

matrix = [[0 for x in range(n)] for y in range(n)] 

for i in graph.keys():
    j = graph.get(i)
    for k in j:
        if k is not '':
            matrix[int(i)][int(k)]=1
print(matrix)

temp_matrix = copy.deepcopy(matrix)
c = [1 for x in range(n)]

A=[]
for i in range(0,n):
    for j in range(0,n):
        if matrix[i][j] == 1:
            if (temp_matrix[i][j]==1) and (temp_matrix[j][i]==1):
                print(i,j)
                temp=[0 for x in range(n)]
                temp[i],temp[j]=1,1
                A.append(temp)
                temp=[0 for x in range(n)]
                temp[i],temp[j]=-1,-1
                A.append(temp)
                temp_matrix[i][j]=0
                temp_matrix[j][i]=0
#A = [[-3, 1], [1, 2]]
#b = [6, 4]

print("The matrix for equations is : ")
for i in range(0,len(A)):
    print(A[i])
b=[]
for i in range(int(len(A)/2)):
    b.append(2)
    b.append(-1)

bo=[]
print(b)
#print(c)
for i in range(0,n):
    bo.append((0,1))

res = linprog(c, A_ub=A, b_ub=b,bounds=bo)
a=res.x

for i in range(0,len(a)):
    if a[i]>=0.5:
        a[i]=1
    else:
        a[i]=0

print("The values for vertex are : ")
print(a)

print("The sum of cardinality of set of vertex-cover is : ")
print(sum(a))
