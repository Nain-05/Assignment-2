import random
arr=[]
for i in range(0,100):
    arr.append(random.randint(0,1000))
Max_val=arr[0]
Min_val=arr[0]
for num in arr:
    N=num
    print(str(N) + " at INDEX " + str(arr.index(N)))
for i in range(0,len(arr),1):
    if arr[i]>Max_val:
        Max_val= arr[i]
    if arr[i]<Min_val:
        Min_val=arr[i]
print("Maximum Value: "+str(Max_val) + " at INDEX " + str(arr.index(Max_val)) )
print("Minimum Value: "+str(Min_val) + " at INDEX " + str(arr.index(Min_val)) )
for j in arr:
    Mean=(sum(arr))/len(arr)
print("Mean Value: ",Mean)