# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:     
        output = []
        myTree = defaultdict(list)
        
        def traverse(root, myTree, output):
            while not (root.left==None and root.right == None):                
                left = None
                right = None
                if root.left is not None:
                    left = traverse(root.left, myTree, output)
                elif root.right is not None:
                    right = traverse(root.right, myTree, output)
                else:
                    return None

                if (root.val, left, right) in myTree:
                    if [root.val, left, right] not in output:
                        temp = [root.val]
                        if left is not None:
                            temp.append(left)
                        if right is not None:
                            temp.append(right)
                        
                        output.append([temp])
                else:
                    myTree[(root.val, left, right)] = 1
                
                return root.val
        
        val = traverse(root, myTree, output)

        return output