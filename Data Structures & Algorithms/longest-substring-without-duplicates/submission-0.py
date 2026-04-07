class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        left=0
        max_len=0

        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[i])
            max_len=max(max_len,i-left+1)
        return max_len

        