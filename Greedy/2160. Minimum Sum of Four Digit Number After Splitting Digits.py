# please note that here i have implemented the solution as a general solution so that you can do this for any number of digits
# if you want to do this for only 4 digits then you can simply do this by taking the first two digits and the last two digits and then add them
# this will always have time 


#time complexity: O(nlogn)
#space complexity: O(n)




class Solution:
    def minimumSum(self, num: int) -> int:
        x=[int(i) for i in str(num) ] 
        x.sort()   
        p1,p2=0,0
        for i in range(0,len(x),2):
            p1=p1*10+x[i]
            p2=p2*10+x[i+1]
        return p1+p2
hey=Solution()
print(hey.minimumSum(1234))