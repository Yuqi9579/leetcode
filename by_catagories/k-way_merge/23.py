'''
Merge k sorted lists
Hard

给k个排过序的list，将他们从小到大merge
思路：divide and conquer, priority queue(最小堆)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        prev = dummy
        while(l1 and l2):
            if l1.val <= l2.val:
                prev.next = l1
                prev = prev.next
                l1 = l1.next
            else:
                prev.next = l2
                prev = prev.next
                l2 = l2.next
        if l1 == None:
            prev.next = l2
        if l2 ==None:
            prev.next = l1
        return dummy.next
            