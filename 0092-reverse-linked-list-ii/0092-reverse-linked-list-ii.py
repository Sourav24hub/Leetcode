class Solution(object):
    def reverseBetween(self, head, left, right):
        travel = 1
        curr = head
        prv = None
        while travel:
            if travel == left:
                prev = None
                lft = curr
                while travel <= right:
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                    travel += 1
                if left == 1:
                    lft.next = curr
                    return prev
                prv.next = prev
                lft.next = curr
                break
            travel += 1
            prv = curr
            curr = curr.next
        return head