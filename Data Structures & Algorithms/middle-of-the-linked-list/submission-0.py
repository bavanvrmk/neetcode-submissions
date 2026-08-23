# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        p1,p2=head,head
        while p2.next:
            p1=p1.next
            p2=p2.next.next
            if not p2:
                return p1
        return p1