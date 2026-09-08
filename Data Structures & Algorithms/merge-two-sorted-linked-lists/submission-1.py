# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return list1
            
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1

        dummyHead = ListNode()
        curr = dummyHead

        if list1.val <= list2.val:
            curr=list1
            list1 = list1.next
        else:
            curr=list2
            list2 = list2.next

        dummyHead.next = curr

        while list1 or list2:
            if not list2 and list1:
                curr.next=list1
                curr = curr.next
                list1 = list1.next
            elif not list1 and list2:
                curr.next=list2
                curr = curr.next
                list2 = list2.next
            elif list1.val <= list2.val:
                curr.next=list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next=list2
                curr = curr.next
                list2 = list2.next
        
        return dummyHead.next
        




            
