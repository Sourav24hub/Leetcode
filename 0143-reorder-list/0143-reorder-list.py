class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return head
        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        prev = None
        curr = head2
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head2 = prev
        head1 = head
        while head1 and head2:
            nxt1 = head1.next
            head1.next = head2
            nxt2 = head2.next
            head2.next = nxt1
            head1,head2 = nxt1,nxt2
        return head