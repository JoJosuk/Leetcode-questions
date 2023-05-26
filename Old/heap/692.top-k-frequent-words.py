#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        a={}
        for i in words:
            if i in a:
                a[i]+=1
            else:
                a[i]=1

       
        res=sorted(a,key=lambda x:(-a[x], x))
        return res[:k]
# @lc code=end

