def count_beautiful_subsets(nums, k):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if abs(nums[i] - nums[j]) != k:
                dp[i] += dp[j]
    return sum(dp)

print(count_beautiful_subsets([2,4,6],2))