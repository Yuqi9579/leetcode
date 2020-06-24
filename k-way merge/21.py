'''
Merge two sorted list
Easy 

Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.
输入的链表本身是排过序的

IN: 1->2->4, 1->3->4
OUT: 1->1->2->3->4->4
'''


class ListNode():
    '''
    Defination for a singly linked list
    '''
    def __init__(self, val):
        self.val = val
        self.next = next

class Solution():
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        prev = dummy # 从第一个节点开始比较的链表常常会加一个dummy node，最后返回dummy.next
        while(l1 and l2): # 当链表不为空
            if l1.val <= l2.val:
                prev.next = l1 # 改变ListNode.next会改变内存中链表的走向
                prev = prev.next # 赋值是不会改变内存中链表的走向的，只是给一个节点赋予了新的名字prev
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
            