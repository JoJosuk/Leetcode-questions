print('hell')
def add(x,y):
    while y:
        carry=x & y
        x=x^y
        y=carry<<1
    return x
a,b=map(int,input().split())
res=0
while b :
    if b & 1 :
        res=add(res,a)
    a=a << 1
    b=b >> 1
print(res)
