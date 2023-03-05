import math
q=[1,4,3,2]
flag=1
s=sorted(q)
bribe=0
for i in range(len(q)-1,-1,-1):
    target=q[i]-1
    print('target',target,q[i])
    if abs(target-i)>2 :
        print('chaotic')
        flag=0
    else:
        print(i)
        for j in range(target,i):
            if q[j]>q[i]:
                q[j],q[i]=q[i],q[j]
                print('swap',q[j],q[j+1])
                bribe+=1
            print(q[j],q[j+1])
if flag:print('nonchaotic',bribe,math.ceil(bribe/2))
    

    