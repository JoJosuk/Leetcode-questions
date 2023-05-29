class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start=0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start]=nums[i]
                start+=1
        while(start<=i):
            nums[start]=0
            start+=1
        return nums
hey=Solution()
print(hey.moveZeroes([0,1,0,3,12]))