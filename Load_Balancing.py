import copy
loads = [2,3,4,6,2,2]
n=3
m = len(loads)

def find_loads(loads,n,m,lo1):
    final_loads=[]
    machine_loads=[]
    for i in range(0,n):
        load=[]
        load.append(lo1[i])
        machine_loads.append(loads[i])
        final_loads.append(load)
    
    for i in range(n,m):
        l=min(machine_loads)
        ind = machine_loads.index(l)
        final_loads[ind].append(lo1[i])
        machine_loads[ind]+=(loads[i])

    return (machine_loads,final_loads)

def reverse_list(loads):
    lo=copy.deepcopy(loads)
    lo.sort(reverse=True)
    return lo

print("Method 1 : ")
lo1 = [i for i in range(0,m)]
machine_loads,final_loads = find_loads(loads,n,m,lo1) 
for i in range(0,n):
    print("Load on machine",i+1,"is :",machine_loads[i],". Job assigned to machine",i+1,"are : ",final_loads[i])

print("\nMethod 2 : ")
lo2=reverse_list(loads)
lo1 = copy.deepcopy(loads)
lo4 = [i for i in range(0,m)]
lo3=[]
for i in lo2:
    temp=lo1.index(i)
    temp1=lo4[temp]
    lo3.append(temp1)
    del lo1[temp]
    del lo4[temp]
machine_loads,final_loads = find_loads(reverse_list(loads),n,m,lo3)
for i in range(0,n):
    print("Load on machine",i+1,"is :",machine_loads[i],". Job assigned to machine",i+1,"are : ",final_loads[i])


def find_loads1(loads,n,m,capacity,lo1):
    machine_loads=[0.0 for i in range(0,n)]
    final_loads=[]
    for i in range(0,n):
        load=[]
        final_loads.append(load)
    for i in range(0,m):
        temp_loads=copy.deepcopy(machine_loads)
        for j in range(0,n):
            temp_loads[j]+= (loads[i]/capacity[j])
        ind=temp_loads.index(min(temp_loads))
        final_loads[ind].append(lo1[i])
        machine_loads[ind]=(temp_loads[ind])
    return (machine_loads,final_loads)

capacity=[1,2,3]
print("\nMethod 3 : ")
lo1 = [i for i in range(0,m)]
machine_loads,final_loads = find_loads1(loads,n,m,capacity,lo1) 
for i in range(0,n):
    print("Load on machine",i+1,"is :",machine_loads[i],". Job assigned to machine",i+1,"are : ",final_loads[i])

print("\nMethod 4 : ")
lo2=reverse_list(loads)
lo1 = copy.deepcopy(loads)
lo4 = [i for i in range(0,m)]
lo3=[]
for i in lo2:
    temp=lo1.index(i)
    temp1=lo4[temp]
    lo3.append(temp1)
    del lo1[temp]
    del lo4[temp]
machine_loads,final_loads = find_loads1(reverse_list(loads),n,m,capacity,lo3) 
for i in range(0,n):
    print("Load on machine",i+1,"is :",machine_loads[i],". Job assigned to machine",i+1,"are : ",final_loads[i])
