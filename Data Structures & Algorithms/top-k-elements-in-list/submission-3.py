class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        result = sorted(count_map.keys(), key=lambda x:count_map[x], reverse=True)

        return result[:k]
       