class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        mod=10**9+7
        length =len(types)
        @cache
        def dp(i,score):
            if score==target:
                return 1
            if i>=length or score>target:
                return 0
            count,typea=types[i]
            result=0
            for j in range(0,count+1):
                result+=dp(i+1,score+j*typea)
            return result%mod

            
        return dp(0,0)