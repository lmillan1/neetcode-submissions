from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # freq of each letter and group them 
        anagrams = defaultdict(list)

        for word in strs:
            # count freq of each leter
            count = [0] * 26
            for c in word:
                count[ord(c)- ord('a')] += 1
            
            key = tuple(count)
            anagrams[key].append(word)
        return list(anagrams.values())
        
        
        # anagrams = defaultdict(list)

        # for word in strs:
        #     key = tuple(sorted(word))
        #     anagrams[key].append(word)

        # return list(anagrams.values())
        