"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""

## 1
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if nums1 is None or nums2 is None:
            return None

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        nums3 = []

        for num in nums1:
            if num in nums2:
                nums3.append(num)
                nums2.remove(num)
        return nums3        

## 2
from collections import Counter

class Solution2:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if nums1 is None or nums2 is None:
            return None

        c = Counter(nums1)
        nums3 = []
        for num in nums2:
            if c[num] > 0:
                nums3.append(num)
                c[num] -= 1
        return nums3
        
## 3

class Solution3:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if nums1 is None or nums2 is None:
            return None

        i, j = 0, 0
        nums1, nums2 = sorted(nums1), sorted(nums2)
        nums3 = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1    
            else:
                nums3.append(nums1[i])
                i += 1
                j += 1
        return nums3


nums1, nums2 = [1, 3, 3], [3]
obj = Solution()
print(obj.intersect(nums1, nums2))

nums1, nums2 = [1, 3, 3], [3, 3, 5]
obj = Solution2()
print(obj.intersect(nums1, nums2))        

nums1, nums2 = [3, 6, 6], [1, 6]
obj = Solution3()
print(obj.intersect(nums1, nums2))   