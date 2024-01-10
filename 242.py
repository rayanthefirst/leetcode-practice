class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_val = [0] * 26
        for c in s:
            s_val[ord(c) - ord("a")] += 1

        t_val = [0] * 26
        for c in t:
            t_val[ord(c) - ord("a")] += 1

        if s_val != t_val:
            return False

        return True
