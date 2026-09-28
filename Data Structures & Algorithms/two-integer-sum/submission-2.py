class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            nums_dict[i] = nums[i]
            if diff in nums_dict.values() and nums.index(diff) != i:
                return [nums.index(diff),i]
            
               
            
        