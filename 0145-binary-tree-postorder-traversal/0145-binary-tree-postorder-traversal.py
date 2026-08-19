class Solution(object):
    def __init__(self):
        self.ans = []
    
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.val)

    def postorderTraversal(self, root):
        self.postorder(root)
        return self.ans