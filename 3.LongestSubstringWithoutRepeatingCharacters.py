"""Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_str = ""
        max_length = -1

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1    
        for c in s:
            if c in temp_str:
                temp_str = temp_str[temp_str.index(c) + 1:]
            temp_str += c
            max_length = max(max_length, len(temp_str))    
        return max_length      

 
    # def lengthOfLongestSubstring(self, str):
    #     test = ""
    #     # Result
    #     maxLength = -1
        
    #     # Return zero if string is empty
    #     if (len(str) == 0):
    #         return 0
    #     elif(len(str) == 1):
    #         return 1
    #     for c in list(str):
    #         current = "".join(c)
            
    #         # If string already contains the character
    #         # Then substring after repeating character
    #         if (current in test):
    #             test = test[test.index(current) + 1:]
    #         test = test + "".join(c)
    #         maxLength = max(len(test), maxLength)
    #     return maxLength
 
 
sol = Solution()

s = "abcadabcdefbb"
print(sol.lengthOfLongestSubstring(s))
