#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dicti={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if i in dicti.values():
                stack.append(i)
            else:
                if not stack:return False
                if stack[-1]!=dicti[i]:return False
                stack.pop()
        if not stack: return True
        return False
# @lc code=end

