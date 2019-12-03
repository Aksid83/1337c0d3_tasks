"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# Solution 1
def twoSum_v1(self, nums: list([int]), target: int) -> list([int]):
        result = []
        for i in range(len(nums)):
           if target - nums[i] in nums:
               result.append(i)
        return result

# Solution 2. BEST     
def twoSum_v2(self, nums: list([int]), target: int) -> list([int]):
        maps = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in maps:
                return [maps[diff], i]
            maps[nums[i]] = i
