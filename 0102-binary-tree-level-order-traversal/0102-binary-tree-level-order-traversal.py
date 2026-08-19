class LQueue:
    def __init__(self):
        self.que = []
        self.front = -1
        self.length = 0
    def qsize(self):
        return self.length
    def push(self,data):
        if self.front == -1:
            self.front = 0
        self.que.append(data)
        self.length += 1
    def pop(self):
        if self.length == 0:
            return
        element = self.que[self.front]
        self.front += 1
        self.length -= 1
        return element

class Solution(object):
    def levelOrder(self, root):
        ans = []
        if root is None:
            return ans
        q = LQueue()
        q.push(root)
        ans.append([root.val])

        while q.qsize() > 0:
            level = []
            l = q.qsize()
            for i in range(l):
                frnt = q.pop()
                if frnt.left is not None:
                    q.push(frnt.left)
                    level.append(frnt.left.val)
                if frnt.right is not None:
                    q.push(frnt.right)
                    level.append(frnt.right.val)
            if len(level) > 0:
                ans.append(level)
        return ans