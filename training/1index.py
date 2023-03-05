i = int(input("enter the number of rows"))
matrix = [list(map(int,input().split())) for y in range(i)]
print(matrix)
n=10
listi= [0 for i in range(10)]
for i in matrix:
    a,b,k =i
    listi[a]+=k
    listi[b]-=k
curr =0
maxval=0
for i in listi:
    curr=curr+i
    maxval=max(maxval,curr)


print(maxval)
