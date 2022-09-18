"""Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 https://leetcode.com/problems/pascals-triangle/

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal_arr = []
        for i in range(numRows):
            # print('' * (numRows-i))
            pascal_arr.append(list(map(str, str(11**i))))
        
        return pascal_arr

obj = Solution()
print(obj.generate(numRows=6))