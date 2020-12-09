# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = ListNode(0)
        result_tail = result
        carry = 0
        
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2+carry, 10)
            
            result_tail.next = ListNode(out)
            result_tail = result_tail.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return result.next




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Merge two sorted linked lists and return it as a new sorted list. 
    The new list should be made by splicing together the nodes of the first two lists.
    """
    # """
    # Recursion
    # Time complexity : O(n + m)
    # """
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     if l1 is None:
    #         return l2
    #     elif l2 is None:
    #         return l1
    #     elif l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2
     
    """
    Iteration 
    # Time complexity : O(n + m)
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        result_tail = result

        while l1 and l2:
            if l1.val <= l2.val:
                result_tail.next = l1
                l1 = l1.next
            else:
                result_tail.next = l2
                l2 = l2.next

            result_tail = result_tail.next
            
        result_tail.next = l1 if l1 is not None else l2
        return result.next



class Solution:
    """
    Reverse a singly linked list.
    Example:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL
    """
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            
            curr = head
            
            head = head.next
            
            curr.next = prev
            
            prev = curr
        
        return prev
        
