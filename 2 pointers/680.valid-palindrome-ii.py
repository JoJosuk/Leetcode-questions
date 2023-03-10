#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        flag=1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                if l+1==r:
                    return True
                if s[l+1:r+1]!=s[l+1:r+1][::-1] and s[l:r]!=s[l:r:][::-1]:
                    print(s[l+1:r+1],s[l:r])
                    return False
                else:
                    return True
        return True

        
# @lc code=end

