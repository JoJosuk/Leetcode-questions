def rob( nums):
    prev = curr = 0
    for value in nums:
        prev, curr = curr, max(prev + value, curr)
    return curr
def deleteAndEarn( nums ):
    length=max(nums)
    dp=[0]*(length+1) 
    for i in nums:
        dp[i]+=i

    return rob(dp)
print(deleteAndEarn([2,1,32,4]))