class Solution:
    def generate(self, numRows: int):
        a=[None]*numRows
        for i in range(numRows):
            a[i]=[1]*(i+1)
        
        for i in range(2,numRows):
            for j in range(1,i):
                a[i][j]=a[i-1][j]+a[i-1][j-1]
        return a
    
hey=Solution()
print(hey.generate(5))