l1=[1,2,3,4,5,6,7,8,90]
l2=[2,3,4,5,99]
l3=l1+l2
print('si',sorted[l3])
i,j=0,0
l3=[]
while i< len(l1) and j <len(l2):
    if l1[i]==l2[j]:
        l3.extend([l1[i],l2[j]])
        i+=1
        j+=1
    elif l1[i]>l2[j]:
        l3.append(l2[j])
        j+=1
    else:
        l3.append(l1[i])
        i+=1

while i< len(l1) :
    l3.append(l1[i])
    i+=1
while j <len(l2):
    l3.append(l2[j])
    j+=1
print(l3)




