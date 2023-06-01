# hey let me explain this solution method, as there is intersection of listnodes here they both should have the same memory
# so by using cache here we are not using for dp we get the id of prev
# this is not a proper method
# the solution is correct tho



from functools import cache
@cache
class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        stacka =[]
        stackb=[]
        while headA or headB:
            if headA:
                stacka.append(headA)
                headA=headA.next
            if headB:
                stackb.append(headB)
                headB=headB.next
        prev=None
        while stacka and stackb:
            a=stacka.pop(-1)
            if a == stackb.pop(-1):
                prev=a
            else:
                return prev
        return prev
            
        
                
            
hey=Solution()
print(hey.getIntersectionNode(ListNode(4,ListNode(1,ListNode(8,ListNode(4,ListNode(5))))),ListNode(5,ListNode(0,ListNode(1,ListNode(8,ListNode(4,ListNode(5))))))).val)