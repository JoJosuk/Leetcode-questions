
'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        idk=0
        for i in collections.Counter(s).values():
            idk+=(i//2)*2
            if idk%2==0 and i%2==1:
                idk+=1
        return idk