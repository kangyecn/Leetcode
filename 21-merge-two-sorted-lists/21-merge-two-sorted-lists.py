# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list1.val is None:
            if list2 is None or list2.val is None:
                return
            return list2
        if list2 is None or list2.val is None:
            return list1
        if list1.val > list2.val:
            return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
        return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))