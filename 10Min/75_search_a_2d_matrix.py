# hey you can use a binary search over matrix that will make it abinary search over a binary search.....super dope but i aint doing it consider me lazy....or i dont like over engineering bite me idc


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        for i in matrix:
            if i[-1]==target:
                return True
            elif i[-1]>target:
                low,high=0,len(i)-1
                
                while(low<=high):
                    mid=(low+high)//2
                    if i[mid]==target:
                        return True
                    elif i[mid]<target:
                        low=mid+1
                    else:
                        high=mid-1
                return False
            else:
                continue
            
hey=Solution()
print(hey.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3))