class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp={}
        for i in strs:
            key="".join(sorted(i))
            if key not in grp:
                grp[key]=[]
            grp[key].append(i)
        return list(grp.values())