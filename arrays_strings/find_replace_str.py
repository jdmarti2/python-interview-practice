"""Find And Replace in String.

Task: You are given a 0-indexed string s that you must perform k replacement
operations on. The replacement operations are given as three 0-indexed parallel
arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

    1. Check if the substring sources[i] occurs at index indices[i] in the
    original string s.
    2. If it does not occur, do nothing.
    3. Otherwise if it does occur, replace that substring with targets[i].

All replacement operations must occur simultaneously, meaning the replacement
operations should not affect the indexing of each other. The testcases will be
generated such that the replacements will not overlap.

Return the resulting string after performing all replacement operations on s.
A substring is a contiguous sequence of characters in a string.
"""


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Start from the right and replace substrings
        ans = s
        for i, a, t in sorted(zip(indices, sources, targets), reverse=True):
            if s[i: i + len(a)] == a:
                ans = ans[:i] + t + ans[i + len(a):]
        return ans
