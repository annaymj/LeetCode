# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        num_list = self.binaryTreePaths(root)
        
        result = 0
        for num in num_list:
            result += int(str(num),2)
        return result
    
    def binaryTreePaths(self,root): 
        if root == None:
            return []
        
        if (root.left == None and root.right == None):
            return [str(root.val)]
        
        # otherwise try both substrees
        return [str(root.val) + num for num in self.binaryTreePaths(root.right) + self.binaryTreePaths(root.left)]