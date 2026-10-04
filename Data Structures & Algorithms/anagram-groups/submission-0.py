from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            # Create a character count array of size 26 for 'a' through 'z'
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Convert array to a tuple so it can be used as a dictionary key
            ans[tuple(count)].append(s)
            
        return list(ans.values())