"""

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 
Follow up: Could you find an algorithm that runs in O(m + n) time?


Time Complexity: O(m+n) (since each character is processed at most twice).
Space Complexity: O(1) (since countT and countS store at most 52 characters, which is constant).

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Approach:
# 1. Use a hashmap `countT` to store character frequencies of `t` and another hashmap `countS` to track character counts in the sliding window.
# 2. Expand the right pointer (`r`) to include characters in `s`, and shrink the left pointer (`l`) when all required characters are in the window.
# 3. Update the minimum window size whenever a valid window is found and return the smallest substring containing all characters of `t`.


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        countT = {}

        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)

        countS = {}

        need = len(countT)
        have = 0

        l = 0
        res, res_len = [-1, -1], float("inf")

        for r in range(len(s)):
            ch = s[r]
            countS[ch] = 1 + countS.get(ch, 0)

            if ch in countT and countS[ch] == countT[ch]:
                have += 1

            while have == need:
                # update window
                if (r-l+1) < res_len:
                    res_len = r-l+1
                    res = [l, r]

                # pop left element
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        return s[l:r+1] if res_len != float("inf") else ""


