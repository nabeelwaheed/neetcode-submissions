class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_S = {}
        hash_T = {}

        for i in range(len(s)):
            hash_S[s[i]] = 1 + hash_S.get(s[i], 0)
            hash_T[t[i]] = 1 + hash_T.get(t[i], 0)

        for c in hash_S:
            if hash_S[c] != hash_T.get(c, 0):
                return False
        
        return True