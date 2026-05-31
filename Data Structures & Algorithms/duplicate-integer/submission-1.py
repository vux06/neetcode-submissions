class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return (False if sorted(nums) == sorted(list(set(nums))) else True)
         