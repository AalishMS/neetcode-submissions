class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDuplicate = set(nums)
        if len(noDuplicate) != len(nums):
            return True
        else:
            return False
                      