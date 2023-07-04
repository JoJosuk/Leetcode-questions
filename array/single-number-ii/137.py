from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = dict(Counter(nums))
        for i in a.keys():
            if a[i] == 1:
                return i

def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Example usage
    nums = [2, 2, 1, 1, 4, 3, 3]
    result = solution.singleNumber(nums)
    print(f"The single number is: {result}")

if __name__ == "__main__":
    main()

