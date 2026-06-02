class Solution:
    def multi(self, arr, idx):
        pro = 1
        for j in range(len(arr)):
            if j != idx:
                pro *= arr[j]
        return pro

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = []
        for i in range(len(nums)):
            x.append(self.multi(nums, i))
        return x