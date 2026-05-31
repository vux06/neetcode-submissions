class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        result = []
        for i in nums:
            a[i] = 0
        for i in nums:
            a[i] += 1
        return list(dict(sorted(a.items(), key=lambda item: item[1], reverse=True)).keys())[:k]
            