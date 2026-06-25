# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_linked_list(self, head: ListNode) -> ListNode:
        # handle empty list or single-node list
        if head is None or head.next is None:
            return head

        # recursively reverse the rest of the list
        new_head = self.reverse_linked_list(head.next)

        # at this point head.next is the tail of the reversed sublist;
        # point its next back to head
        head.next.next = head
        # detach head from the rest
        head.next = None

        # new_head is the head of the reversed list
        return new_head

    def reverse_linked_list_ii(self, head: ListNode, left: int, right: int) -> ListNode:
        # handle empty list or single-node list
        if head is None or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        # move prev to node before left
        for _ in range(left - 1):
            prev = prev.next

        # identify sublist boundaries
        sublist_head = prev.next
        sublist_tail = sublist_head
        for _ in range(right - left):
            sublist_tail = sublist_tail.next

        after = sublist_tail.next

        # detach sublist from original list
        sublist_tail.next = None

        # reverse sublist
        reversed_head = self.reverse_linked_list(sublist_head)

        #reconnect
        prev.next = reversed_head
        sublist_head.next = after

        return dummy.next

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        return self.reverse_linked_list_ii(head, left, right)