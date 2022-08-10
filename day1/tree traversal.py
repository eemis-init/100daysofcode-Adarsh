from queue import *
import queue
class BinaryTree:
    class _Node:
        __slots__='element','left','right'
        def __init__(self,element,left=None,right=None) -> None:
            self.element=element
            self.left=left
            self.right=right
    
    def __init__(self):
        self.root=None
        self.size=0
    def makeTree(self,e,left,right):
        self.root=self.Node(e,left.root,right.root)
        left.root=None
        right.root=None
    def levelorder(self):
        Q=queue()
        t=self.root
        Q.enqueue(t)
        while not Q.size()==0:
            t=Q.dequeue()
            if t.left:
                print(t.left.element,end=" ")
                Q.enqueue(t.left)
            if t.right:
                print(t.right.element,end=" ")
                Q.enqueue(t.right)
    def preorder(self,troot):
        if troot:
            print(troot.element,end="--")
            self.preorder(troot.left)
            self.preorder(troot.right)
    def postorder(self,troot):
        if troot:
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.element,end="--")
    def inorder(self,troot):
        if troot:
            self.inorder(troot.right)
            print(troot.element,end="--")
            self.inorder(troot.right)

