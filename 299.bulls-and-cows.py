#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s,g=Counter(secret),Counter(guess)
        a=sum(i==j for i,j in zip(secret,guess))
        res=str(a)+'A'+str(sum((s&g).values())-a)+'B'
       
        return res
                
        
# @lc code=end

