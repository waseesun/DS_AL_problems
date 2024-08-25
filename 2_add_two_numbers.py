# Problem: https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        sum_l = ListNode()
        curr_l = sum_l
        i = 0
        j = 0
        carry = 0
        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                addi = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1 != None:
                addi = l1.val + carry
                l1 = l1.next
            elif l2 != None:
                addi = l2.val + carry
                l2 = l2.next
            curr_l.val = addi % 10
            carry = addi // 10
            if (l1 != None or l2 != None) or carry != 0:
                curr_l.next = ListNode(carry)
                curr_l = curr_l.next

        return sum_l