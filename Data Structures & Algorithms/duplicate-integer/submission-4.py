class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums) # copy list to set to have unique elements
        return len(nums) != len(nums_set)
        