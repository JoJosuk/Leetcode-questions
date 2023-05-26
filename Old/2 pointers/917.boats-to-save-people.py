#
# @lc app=leetcode id=953 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        l,r=0,len(people)-1
        res=0
        while l<r:
            cursum=people[l]+people[r]
            if cursum>limit:
                r-=1
                res+=1
            else:
                l+=1
                r-=1
                res+=1
        if l==r:res+=1
        return res
        
# @lc code=end

