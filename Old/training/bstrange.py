class Solution:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def insert(valu,node):
    if valu>node.val:
        if node.right!=None:insert(valu,node.right)
        else:node.right=Solution(valu)
    if valu<node.val:
        if node.left!=None:insert(valu,node.left)
        else:node.left=Solution(valu)
def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.val,end=",")
        inorder(root.right)
root=Solution(10)
insert(2,root)
insert(11,root)
insert(64,root)
insert(1,root)
insert(8,root)


def ranger(head,l,r):
    while head:
        if l<head.val<r:
            return head
        elif head.val>l and head.val>r :
            head=head.right
        elif head.val<l and head.right<r:
            head=head.left
head=root
l=4
r=10
header=ranger(head,l,r)
print(header.val)
