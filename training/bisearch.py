lister=[1]*10+[2]*30
print(lister)
n=2
l,r=0,len(lister)-1
while l<r:
    mid=(l+r)//2
    if lister[mid]>=n:
        r=mid
    else:
        l=mid+1
print(l)


print(lister)