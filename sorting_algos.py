#Selection Sorting
# get the minimum and swap
arr = [13,46,24,52,20,9]
n = len(arr)
for i in range(n-1):
    mini = i
    for j in range(i+1,n):
        if(arr[mini] > arr[j]):
            mini = j
    arr[mini],arr[i] = arr[i],arr[mini]
print(arr)


#bubble sort
# max element is pushed to the last by ajuscent swaping
# arr = [13,46,24,52,20,9]
arr = [9, 13, 20, 24, 46, 52]
n = len(arr)
for i in range(n-1,0,-1):
    flag = False
    for j in range(i):
        if(arr[j] > arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            flag = True
    if(flag == False):
        print(arr)
        break

print(arr)


# Insertion sort
arr = [13, 46, 24, 52, 20, 9]
n = len(arr)
for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print(arr)