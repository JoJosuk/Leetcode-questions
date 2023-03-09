#
# @lc app=leetcode id=2647 lang=python3
#
# [2584] Split the Array to Make Coprime Products
#

# @lc code=start
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        print('ha')
        p=[nums[-1]]
        print('j')
        for i in nums[-2::-1]:
            p.append(p[-1]*i)
        p=p[-2::-1]
        pp=1
        print('o')
        for j,i in enumerate(nums[:-1]):
            pp=pp*i
            if math.gcd(pp,p[j])==1:
                return j
        print(i)
        return -1
        
# @lc code=end

