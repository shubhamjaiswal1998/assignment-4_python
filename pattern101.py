def f1(n):
    for i in range(0,n):
        for j in range(0,i):
            value=(i+j)%2
            if value==0:
                print("0",end="")
            else:
                print("1",end="")    
        print()    
f1(6) 

def f2(n): #diomond pattern
    for i in range(0,n):
        for j in range(0,n-i):
            print(" ",end="")
        for j in range(0,2*i-1):
            print("*",end="") 
        print()  
    for i in range(n,0,-1):  #decreasing loop
        for j in range(0,n-i):
            print(" ",end="")
        for j in range(0,2*i-1):
            print("*",end="")
        print()            
f2(6)       

#function call with deffrently
res=(lambda a,b:b-2*a)
print(res(1,11))# 11-2*1=9

res2=(lambda x,y:y-2*x)(1,11)
print(res2)#9  same output will give

def removeth(str1, k):
    if k>len(str1):
        return str1
    str2=""
    for i in range(0,len(str1)):
        if i!=k:
            str2=str2+str1[i]
    return str2
print(removeth("python",2))#pyhon
print(removeth("python",10)) # python

def less_than(list1,element):
    list2=[]
    for i in list1:
        if i<element:
            list2.append(i)
    return list2
print(less_than([1, -2, 0, 5, -3],0))  #[-2,-3]




