
def fib(n):
    n1,n2,i=0,1,1
    if n==0:return n1 
    elif n==1: return n2
    else :
        while i<n:
            temp=n1+n2
            n1,n2=n2,temp
            i+=1
        return temp

def fibo(n):
    if n<2:return n
    else:
        return fibo(n-1)+fibo(n-2)
print(fib(8))
print(fibo(99))
