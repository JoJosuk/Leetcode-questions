#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
import collections
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sdict=collections.Counter(s[:len(p)-1])
        pdict=collections.Counter(p)
        start=0
        res=[]
        for i in range(len(p)-1,len(s)):
            sdict[s[i]]+=1
            if sdict==pdict:
                res.append(start)
            sdict[s[start]]-=1
            if sdict[s[start]] ==0:
                del sdict[s[start]]
            start+=1
        return res
        
                        

                        


            
        
# @lc code=end

