"""Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
"""

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createNode(self, child):
        return TreeNode(child)

    def insertNode(self, root, child):
        if child < root.val:
            if root.left:
                self.insertNode(root.left, child)
            else:
                root.left = TreeNode(child)
        if child > root.val:
            if root.right:
                self.insertNode(root.right, child)
            else:
                root.right = TreeNode(child)                               

    def deleteNode(self, key: int):
        pass

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.val)
            self.inorderTraversal(root.right)
        # traversed_elements = []

        # if root.left:
        #     traversed_eleements += self.inorderTraversal(root.left)
        
        # traversed_elements.append(root.val)

        # if root.left:
        #     traversed_elements += self.inorderTraversal(root.right)

        # return traversed_elements

obj = Solution()
# root = obj.createNode(5)
# print(root.val)
# obj.insertNode(root, 3)
# obj.insertNode(root, 2)
# obj.insertNode(root, 4)
# obj.insertNode(root, 6)
# obj.insertNode(root, 7)
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)


print("Before deleting node: ", obj.inorderTraversal(root))

obj.deleteNode(5)

print("After deleting node: ",obj.inorderTraversal(root))