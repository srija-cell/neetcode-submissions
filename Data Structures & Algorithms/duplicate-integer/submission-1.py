class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = set(nums)
        if len(nums) == len(data):
            return False
        else:
            return True
