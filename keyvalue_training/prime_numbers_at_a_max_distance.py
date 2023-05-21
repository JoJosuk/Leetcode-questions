import math
def prime(a):
    for i in range(2,int(math.sqrt(a+1))+1):
        if a%i==0:
            return False
    return True
        
a,b,c=map(int,input().split())
if c> b:
    for i in range(a,b+1):
        if prime(i):
            print(abs(i-c))
            exit()
    print(-1)
elif c<a:
    for i in range(b,a-1,-1):
        if prime(i):
            print(abs(i-c))
            exit()
    print(-1)
else:
    
    for i in range(a,c+1):
        if prime(i):
            alarge=i
            flaga=1
            break
        else:
            flaga=0
    for i in range(b,c,-1):
        if prime(i):
            blarge=i
            flagb=1
            break
        else:
            flagb=0
    if flaga==0 and flagb==0:
        print(-1)
    elif flaga==0:
        print(abs(blarge-c))
    elif flagb==0:
        print(abs(alarge-c))
    else:
        if abs(alarge-c)>abs(blarge-c):
            print(abs(alarge-c))
        else:
            print(abs(blarge-c))