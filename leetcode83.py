class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        
        if not curr:
            return curr
            
        next = curr.next
        
        while not next:
            print curr, next
            if curr.val == next.val:
                curr.next = next.next
                next = next.next
            else:
               curr = curr.next
               next = next.next
        return head

l1 = ListNode(1)
l2 = ListNode(1)
l1.next = l2
l3 = ListNode(1)
l2.next = l3
print l1, l2, l3
s = Solution()
l = s.deleteDuplicates(l1)
while l:
    print l.val
    l = l.next 