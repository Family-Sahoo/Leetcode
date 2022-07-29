# '''
#     Merge two sorted linked lists and return it as a new sorted 
#     list. The new list should be made by splicing together the 
#     nodes of the first two lists.
#     Example:
#     Input: l1 = [1,2,4], l2 = [1,3,4]
#     Output: [1,1,2,3,4,4]
#     Example:
#     Input: l1 = [], l2 = []
#     Output: []
#     Example:
#     Input: l1 = [], l2 = [0]
#     Output: [0]
#     Constraints:
#         - The number of nodes in both lists is in the range 
#           [0, 50].
#         - -100 <= Node.val <= 100
#         - Both l1 and l2 are sorted in non-decreasing order.
# '''
# #Difficulty: Easy
# #208 / 208 test cases passed.
# #Runtime: 40 ms
# #Memory Usage: 14.3 MB

# #Runtime: 40 ms, faster than 40.63% of Python3 online submissions for Merge Two Sorted Lists.
# #Memory Usage: 14.3 MB, less than 26.66% of Python3 online submissions for Merge Two Sorted Lists.

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoSortedLists(self, list1: ListNode, list2: ListNode) -> ListNode:
#         node1, node2 = list1, list2
#         list3 = ListNode()
#         node3 = list3
#         print("Initial: ", node3.val, node1.next)

#         # while node3:
#         #     if node1 and node2 and node1.val > node2.val:
#         #         node3.next = node2
#         #         node2 = node2.next
#         #         print(node3, node2)
            



# mergeTwoSortedListsObj = Solution()
# print(mergeTwoSortedListsObj.mergeTwoSortedLists([1, 2, 3], [2, 3, 4]))

# initializing lists
test_list1 = [1, 5, 6, 9, 11]
test_list2 = [1, 4, 7, 9, 10]
  
# printing original lists 
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))
  
# using sorted()
# to combine two sorted lists
res = sorted(test_list1 + test_list2)
  
# printing result
print ("The combined sorted list is : " + str(res))