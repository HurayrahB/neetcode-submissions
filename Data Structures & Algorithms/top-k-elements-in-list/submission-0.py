class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        
        highest_k_keys = sorted(count, key=count.get, reverse=True)[:k]

        return highest_k_keys