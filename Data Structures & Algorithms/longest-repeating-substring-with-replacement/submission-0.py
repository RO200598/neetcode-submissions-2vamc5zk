class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        max_freq=0
        max_len=0

        for i in range(len(s)):
            count[s[i]]=1+count.get(s[i],0)

            max_freq=max(max_freq,count[s[i]])

            while (i-left+1)-max_freq>k:
                count[s[left]]-=1
                left+=1
            max_len=max(max_len,i-left+1)
        return max_len
        