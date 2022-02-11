class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dic = {}
        for s in strs:
            temp_s = sorted(s)
            temp_s = tuple(temp_s)
            if temp_s in hash_dic:
                hash_dic[temp_s].append(s)
            else:
                 hash_dic[temp_s] = [s]
        return hash_dic.values()        