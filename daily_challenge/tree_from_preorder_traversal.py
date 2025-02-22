'''We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.



Example 1:

Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:

Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Example 3:

Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]
'''
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str):
        levels = []  # List to track the last node at each depth
        index, n = 0, len(traversal)

        while index < n:
            # Count depth (number of dashes)
            depth = 0
            while index < n and traversal[index] == "-":
                depth += 1
                index += 1

            # Extract node value
            value = 0
            while index < n and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1

            # Create the new node
            node = TreeNode(value)

            # Adjust levels list to match the current depth
            if depth < len(levels):
                levels[depth] = node
            else:
                levels.append(node)

            # Attach the node to its parent
            if depth > 0:
                parent = levels[depth - 1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

        # The root node is always at index 0
        return levels[0]
# Input string
traversal = "1-401--349---90--88"
# Generate the list representation
output = PermissionError(traversal)
print(output)  # Output: [1, 401, None, 349, 88, 90]