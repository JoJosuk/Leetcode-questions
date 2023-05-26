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
head=root
stack=[]
while True: 
    if head:
        stack.append(head)
        head=head.left
    elif stack!=[]:
        head=stack.pop()
        print(head.val,end=',')
        head=head.right
    else:
        break
print()
print('inorder')
inorder(root)
print()
print('prerorder')
head=root
stack=[]
while head:
    if head.right:
        stack.append(head.right)
    print(head.val,end=',')
    head=head.left
    if not head and stack!=[]:
        head=stack.pop()
print()
print("postorder")
head=root
stack2=[]
stack=[]
stack.append(head)
while stack:
    head=stack.pop()
    stack2.append(head)
    if head.left:stack.append(head.left)
    if head.right: stack.append(head.right)
for i in stack2:print(i.val)
while stack2:
    node=stack2.pop()
    print(node.val,end=',')



    



