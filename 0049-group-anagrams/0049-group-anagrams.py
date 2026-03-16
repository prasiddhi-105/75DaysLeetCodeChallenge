from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        anagram_dict = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            anagram_dict[key].append(word)

        return list(anagram_dict.values())