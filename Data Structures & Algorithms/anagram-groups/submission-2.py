class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for s in strs:
            c = sorted(s)
            dict[tuple(c)].append(s)
        
        
        return list(dict.values())