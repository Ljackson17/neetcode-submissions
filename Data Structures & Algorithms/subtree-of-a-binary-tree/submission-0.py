# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue:
            current = queue.pop()
            if self.sameTree(current, subRoot) == True:
                return True
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
        return False

    def sameTree(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
            
        
        