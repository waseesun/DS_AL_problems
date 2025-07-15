# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head):
        n = ListNode(None)
        n.next = head
        current = n
        while current.next:
            if current.next.next:
                temp = current.next
                current.next = current.next.next
                if temp:
                    temp.next = current.next.next
                if current.next:
                    current.next.next = temp
                current = current.next.next
            else:
                current = current.next
            
        return n.next
                
def ls(lst):
    head = ListNode(lst[0])
    current = head
    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next
        
    return head
        

if __name__ == '__main__':
    lst = [1, 2, 3, 4]
    sol = Solution()
    ll_ls = ls(lst)
    head = sol.swapPairs(ll_ls)
    lst = [1]
    ll_ls = ls(lst)
    head = sol.swapPairs(ll_ls)
    lst = [1, 2, 3]
    ll_ls = ls(lst)
    head = sol.swapPairs(ll_ls)
    print("hello")