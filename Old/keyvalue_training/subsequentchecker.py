i,j=0,0
a=input()
b=input()

while(i<len(a)):
    if j>=len(b):
        break
    if a[i]==b[j]:
        i+=1
        j+=1
    else:
        i+=1
if j>=len(b):
    print( True)
else:
    print( False)