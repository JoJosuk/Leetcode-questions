# class Solution:
#     def isPalindrome( s) :
#         length =len(s)
#         l,r=0,len(s)-1
        
#         while l<r:
#             while not s[l].isalnum() and l<r:l+=1
#             while not s[r].isalnum()and l<r:r-=1
#             if s[r].lower()!=s[l].lower():
#                 return False
#             r-=1;l+=1
#         return True
class Solution:
    def isPalindrome( s: str) -> bool:
        r = re.sub(r'[^a-zA-Z0-9]','', s).lower()

        if r == r[::-1]:
            return True
        else:
            return False

print(Solution.isPalindrome('abcdcba'))