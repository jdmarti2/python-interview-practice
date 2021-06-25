"""Find Smallest substring in string containing target string.

Task: Given two strings s and t of lengths m and n respectively, return the
minimum window substring of s such that every character in t (including
duplicates) is included in the window. If there is no such substring, return
the empty string "".
"""


from collections import Counter


class Solution:
    """Smallest window containing substring."""

    def minwindow(self, s, t):
        """Hash via Counter() & use two pointer method to find min window."""
        start = 0
        min_str = ""
        # Get counts and length of char in t
        target_count = Counter(t)
        target_len = len(t)
        # Iterate thru s to find smallest window
        for i in range(len(s)):
            # See if s[i] in t
            if target_count[s[i]] > 0:
                target_len -= 1
            # Its ok it count is negative. It will just be ignored
            target_count[s[i]] -= 1
            while target_len == 0:
                # Check if current selection < min_str
                if not min_str or len(s[start:i + 1]) < len(min_str):
                    min_str = s[start:i + 1]
                # Move start left
                target_count[s[start]] += 1
                if target_count[s[start]] > 0:
                    target_len += 1
                start += 1
        return min_str
