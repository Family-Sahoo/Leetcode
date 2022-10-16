"""Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

from unittest import result


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resultlen = 0

        for i in range(len(s)):
            # Odd Length
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultlen:
                    result = s[l:r+1]
                    resultlen = r - l + 1
                l -= 1
                r += 1


            # Even Length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultlen:
                    result = s[l:r+1]
                    resultlen = r - l + 1
                l -= 1
                r += 1

        return result, resultlen   



sol = Solution()
s = "ababab"
print(sol.longestPalindrome(s))