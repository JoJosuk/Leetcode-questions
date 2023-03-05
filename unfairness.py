arr=[1,4,7,2]
arr=sorted(arr)
print(arr)
k=2
unfair=arr[len(arr)-1]-arr[0]

for i in range(0,len(arr)-k+1):
    if unfair>arr[i+k-1]-arr[i]:
        unfair=arr[i+k-1]-arr[i]
print(unfair)