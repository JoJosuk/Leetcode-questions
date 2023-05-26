class Solution:
    def largestNumber(self, nums) -> str:
        for i in range (0,len(nums)):
            m=i
            s1=str(nums[i])
            for j in range(i+1,len(nums)):
                s2=str(nums[j])

                if s1+s2 <s2+s1:
                    m=j
                    s1=str(nums[j])
            nums[m],nums[i]=nums[i],nums[m]
        if nums[0]==0:
            return '0'
        return (''.join([str(x) for x in nums ]))
hey=Solution()
print(hey.largestNumber([3,30,34,5,9]))


# from functools import cmp_to_key

# class Solution:
#   def largestNumber(self, nums: List[int]) -> str:
#     snums = list(map(lambda x: str(x), nums))
#     def _comp(i, j):
#       if j + i > i + j:
#         return 1
#       else:
#         return -1
#     snums.sort(key=cmp_to_key(_comp))
#     return str(int("".join(snums)))