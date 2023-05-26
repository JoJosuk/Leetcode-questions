class Solution(object):
    def lengthOfLongestSubstring( s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1:
            return len(s)
        l,r=0,1
        maxi=''
        while(l<r and r <=len(s)):
            if (r-l)>len(maxi):
                maxi=s[l:r]
            if r==len(s):
                break
            if s[r] in s[l:r] :
                l+=1
                r=l+1
            else:
                r+=1
        return len(maxi)
    print(lengthOfLongestSubstring("abcabcbb"))