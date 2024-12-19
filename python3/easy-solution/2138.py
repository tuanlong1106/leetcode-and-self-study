"""
2138. Divide a String Into Groups of Size k
    A string s can be partitioned into groups of size k using the following procedure:
    The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each character can be a part of exactly one group.
    For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.
    Note that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s.
    Given the string s, the size of each group k and the character fill, return a string array denoting the composition of every group s has been divided into, using the above procedure.

    Example :
    Input: s = "abcdefghi", k = 3, fill = "x"
    Output: ["abc","def","ghi"]
    Explanation:
    The first 3 characters "abc" form the first group.
    The next 3 characters "def" form the second group.
    The last 3 characters "ghi" form the third group.
    Since all groups can be completely filled by characters from the string, we do not need to use fill.
    Thus, the groups formed are "abc", "def", and "ghi".
"""


from typing import List
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        ans = []
        temp = ""
        j = 0
        for i in range(n):
            temp += s[i]
            j += 1
            if j == k:
                ans.append(temp)
                temp = ""
                j = 0
        if len(temp) != 0:
            temp += fill * (k - j)
            ans.append(temp)
        return ans