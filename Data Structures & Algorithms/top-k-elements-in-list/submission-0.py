class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums =[1, 2, 2, 3, 3, 3] , k = 2

        # dictionary to map each key-> the number and the value -> the number of occurences
        count_map = {}

        for num in nums:
            # we want to get the freq of each number
            count_map[num] = count_map.get(num, 0 ) + 1
            
        # want to use a lambda funciton to sort the keys by their values in the dict
        result = sorted(count_map.keys(), key=lambda x:count_map[x], reverse=True)

        return result[:k]



