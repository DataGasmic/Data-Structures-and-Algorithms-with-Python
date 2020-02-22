class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None
        
        
def getCountOfNode(root,l,h):
    
    if root==None:
        return 0
    if root.data==l and root.data==h:
        return 1
    else:
        if h<root.data:
            return getCountOfNode(root.left,l,h)
        elif l>root.data:
            return getCountOfNode(root.right,l,h)
        else:
            a = getCountOfNode(root.right,l,h)
            b = getCountOfNode(root.left, l,h)
            return a+b+1

        
