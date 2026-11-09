class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        highest_k_keys = sorted(count, key=count.get, reverse=True)[:k]

        return highest_k_keys