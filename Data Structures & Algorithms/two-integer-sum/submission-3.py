class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDict = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevDict:
                return [prevDict[diff],i]
            prevDict[n] = i
        