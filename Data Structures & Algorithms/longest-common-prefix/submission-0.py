class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for i in range(1,len(strs)):
            word=strs[i]
            j=0
            while  j < len(prefix) and j < len(word) and prefix[j]==word[j]:
                j+=1 
            prefix=prefix[:j]
        return prefix