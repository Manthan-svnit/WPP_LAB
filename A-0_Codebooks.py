list= list(map(int,input("enter the number by space: ").split()))
print(list)
span=1
for i in range(1,len(list)-1):
    if(list[i+1]>list[i]):
        span += 1
        print(span)
    elif(list[i]>list[i+1]):
        span=13