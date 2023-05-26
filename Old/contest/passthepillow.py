class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i=1
        for i in range(time):
            if i<n:
                i+=1
            else:
                i-=1
        return 
        