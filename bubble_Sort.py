
#insertion sort
arr = [5,3,4,2,1,2,1]
n = len(arr)
for i in range(1,n):
    j = i
    while(j>0 and arr[j]<arr[j-1]):
        arr[j],arr[j-1] = arr[j-1],arr[j]
        j-=1
print(arr)