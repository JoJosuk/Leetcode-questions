class Solution:
    def minimumTime( time, totalTrips) :
        time.sort()
        l,r=0,10**8
        while l<=r:
            med=(l+r)//2
            print(med)
            trips=sum(med//t for t in time)
            if trips>totalTrips:
                r=med-1
            else:
                l =med+1
        return l
            
    print(minimumTime([1,2,3],5))