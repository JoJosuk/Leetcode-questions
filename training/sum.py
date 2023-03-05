def inti():
    ind ='11123233534654'
    k=6
    summ=0
    l=0
    for r in range(len(ind)):
        summ+=int(ind[r])
        if summ==k:
                return ind[l:r+1]
        while summ>k and l<r:
            summ-=int(ind[l])
            l+=1
            if summ==k:
                return ind[l:r+1]
print(inti()) 