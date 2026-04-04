class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1,t1=sorted(s),sorted(t)
        for i in range(len(s1)):
            if s1[i]!=t1[i]:
                return False
        return True
        