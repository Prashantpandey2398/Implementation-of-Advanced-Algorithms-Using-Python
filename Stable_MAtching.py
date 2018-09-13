import numpy as np
import random
import math
import matplotlib.pyplot as plt

num_test = int(input("Enter the number of testcases : "))

number_list=[]
count_list=[]
for t in range(0,num_test):
    n = int(math.pow(2,t+1))
    pm=[]
    for i in range(0,n):
        temp1=random.sample(range(1,n+1),n)
        pm.append(temp1)
    pw=[]
    for i in range(0,n):
        temp1=random.sample(range(1,n+1),n)
        pw.append(temp1)
    sol=[]
    uem=[]
    output = []
    for i in range(0,n):
        sol.append(0)
        uem.append(i+1)
        output.append(0)
    count=0
    while len(uem)>0:
        for i in uem:
            count+=1
            index=sol[i-1]
            pri=pm[i-1][index]
            sol[i-1]+=1
            if pri in output:
                temp=list(pw[pri-1])
                local=output.index(pri)+1
                s1=temp.index(local)
                s2=temp.index(i)
                if s2<s1:
                    uem.append(local)
                    output[local-1]=0
                    output[i-1]=pri
                    del uem[uem.index(i)]
            else:
                output[i-1]=pri
                del uem[uem.index(i)]

    sum_men=0
    sum_women=0

    for i in range(0,n):
        temp=list(pm[i])
        pri=output[i]
        local=temp.index(pri)
        sum_men+=local
        temp=list(pw[pri-1])
        local=temp.index(i+1)
        sum_women+=local
    print("Number of Mens and Womens : ",n)
    print("Number of proposals : ",count)
    number_list.append(n)
    count_list.append(count)
    print("Average Index of priority of Mens : ",sum_men/n)
    print("Average Index of priority of Womens : ",sum_women/n)
    print()

best_case = number_list.copy()
worst_case = list(np.array(number_list)**2)
plt.plot(number_list,count_list,label="Algorithm")
plt.plot(number_list,best_case,label="Best Case")
plt.plot(number_list,worst_case,label="Worst Case")
plt.axis([2,number_list[len(number_list)-1]+100,2,100000])
plt.xlabel('Input')
plt.ylabel('Time Taken')
plt.title('Stable Matching Problem')
plt.legend()
plt.show()
