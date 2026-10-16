class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        target = {}
        window = {}

        for char in t:
            target[char] = 1 + target.get(char, 0)
        
        have, need = 0, len(target)
        res, resLen = [-1, -1], float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in target and window[c] == target[c]:
                have += 1

            while have == need:
                # Update the result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # Pop the most left from our window
                window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                left += 1
        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""



        
        