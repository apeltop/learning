# https://leetcode.com/problems/group-anagrams/
# 파이썬 알고리즘 인터뷰 책 참고 p.153
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())


print(Solution().groupAnagrams(
    strs=["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]

print(Solution().groupAnagrams(
    strs=["a"]))  # [["a"]]
