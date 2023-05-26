class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start,end=1,x
        while (start<=end):
            mid= (start+end)//2
            if mid*mid==x:
                return mid
            elif mid*mid > x:
                end=mid-1
            elif mid*mid<=x:
                start=mid+1
        return end
                
mysqrt=Solution()
print(mysqrt.mySqrt(8))