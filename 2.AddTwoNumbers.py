"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""


# Definition for singly-linked list.
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_node(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def traversal(self):
        if self.head is None:
            return None
        else:
            current_node = self.head
            while current_node:
                print(current_node.val, end=" -> ")
                current_node = current_node.next


def addTwoNumbers(l1, l2):
    current_node1 = l1.head
    current_node2 = l2.head
    carry = 0
    while current_node1 or current_node2:
        sum = current_node1.val + current_node2.val
        carry = sum // 10
        s = sum % 10
        final_sum = s + carry
        current_node1 = current_node1.next
        current_node2 = current_node2.next

        print(sum)


linkedlist1 = LinkedList()
linkedlist1.insert_node(2)
linkedlist1.insert_node(4)
linkedlist1.insert_node(3)

linkedlist2 = LinkedList()
linkedlist2.insert_node(5)
linkedlist2.insert_node(8)
linkedlist2.insert_node(4)

linkedlist1.traversal()
print()
linkedlist2.traversal()
print()

addTwoNumbers(linkedlist1, linkedlist2)
