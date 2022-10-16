"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums3 = merge_two_arrays(nums1, nums2)

        median = 0
        remainder = len(nums3) % 2
        div = len(nums3) // 2
        if remainder == 0:
            median = (nums3[div] + nums3[div-1]) / 2
        else:
            median = nums3[div]

        return median

def merge_two_arrays(nums1, nums2):
    len1 = len(nums1)
    len2 = len(nums2)
    i, j = 0, 0
    nums3 = []

    while i < len1 and j < len2:
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1
        else:
            nums3.append(nums2[j])
            j += 1
    nums3 += nums1[i:] + nums2[j:]        

    return nums3




sol = Solution()

nums1, nums2 = [1,3], [2]
nums3, nums4 = [1,2], [3,4]
print(sol.findMedianSortedArrays(nums1, nums2))
print()
print(sol.findMedianSortedArrays(nums3, nums4))
print()
arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]
print(sol.findMedianSortedArrays(arr1, arr2))


