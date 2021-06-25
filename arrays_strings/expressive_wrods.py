"""Given a list of query words, return the number of words that are stretchy.

Task: For some given string s, a query word is stretchy if it can be made to be
equal to s by any number of applications of the following extension operation:
choose a group consisting of characters c, and add some number of characters c
to the group so that the size of the group is 3 or more.

If s = "helllllooo", then the query word "hello" would be stretchy because of
these two extension operations:
    query = "hello" -> "hellooo" -> "helllllooo" = s.
"""


def check(s, word):
    """Check if word can be elongated to match s."""
    si, w, s_len, w_len = 0, 0, len(s), len(word)
    if w_len > s_len:
        return False
    # Use two pointers to match characters
    while w < w_len and si < s_len:
        # If char in word and s match, move both pointers right
        if s[si] == word[w]:
            si += 1
            w += 1
        # If char in s is streched, move s char right
        elif s[si] * 3 in (s[si - 2:si + 1], s[si - 1: si + 2]):
            si += 1
        else:
            return False

    if w == w_len and si == s_len:
        return True

    # check if last char in word matches rest of s
    if (word[w_len - 1] * len(s[si:]) == s[si:])\
       and (s[si - 1] * 3 in (s[si - 3:si],
                              s[si - 2: si + 1],
                              s[si - 1: si + 2])):
        return True
    return False


def expressive_words(s, words):
    """Return number of words that can be stretched."""
    num = 0
    for word in words:
        if check(s, word) is True:
            num += 1
    return num
