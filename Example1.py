a=[]
max=input("enter no.of times")
while len(a)<max:
    num=input("enter nos:")
    a.append(num)

def add(a):
    total=0
    for i in a:
        total+=i
    return total
result=add(a)
print result

def average(a):
    res=sum(a)/len(a)
    return res
avg=average(a)
print avg

def highestNumber(a):
    myMax = a[0]
    for num in a:
        if myMax < num:
            myMax = num
    return myMax
print highestNumber (a)

def lowestNumber(a):
    myMin = a[0]
    for i in a:
        if myMin>i:
            myMin = i
    return myMin
print lowestNumber(a)

def secondlargest(a):
    mynum=a[0]
    for i in a:
        if mynum<i:
            mynum=i-1
    return mynum
print secondlargest(a)