class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        # first window
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == window_count[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):

            if matches == 26:
                return True

            # add char
            index = ord(s2[right]) - ord('a')
            window_count[index] += 1

            if window_count[index] == s1_count[index]:
                matches += 1
            elif window_count[index] == s1_count[index] + 1:
                matches -= 1

            # remove char
            index = ord(s2[left]) - ord('a')
            window_count[index] -= 1

            if window_count[index] == s1_count[index]:
                matches += 1
            elif window_count[index] == s1_count[index] - 1:
                matches -= 1

            left += 1

        # 🔥 final window check
        return matches == 26