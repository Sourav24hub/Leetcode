class Solution(object):
    def rotateRight(self, head, k):
        count = 0
        curr = head
        while curr is not None:
            count += 1
            tail = curr
            curr = curr.next
        if count <= 1:
            return head
        k %= count
        if k == 0:
            return head
        cut = count - k
        tail.next = head
        curr = head
        for i in range(cut-1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        return newHead