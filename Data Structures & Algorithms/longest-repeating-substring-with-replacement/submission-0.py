class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        - Keep moving right poniter as long as diff <= k
        - keep moving left pointer until length - maxFreq is greater than k

        """
        res = 0
        left = 0
        count = {}
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res
            