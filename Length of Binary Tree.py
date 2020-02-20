class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None




def binary_tree_height(node):
    
    if node==None:
        return 0
    else:
        
        l_h = binary_tree_height(node.left)
        r_h = binary_tree_height(node.right)
        
        return max(l_h,r_h)+1
    

def bin_tree_from_array(arr, root , i , n):
    
    if i<n:
        
        temp = Node(arr[i])
        root = temp
        
        root.left = bin_tree_from_array(arr , root.left , 2*i+1 ,n)
        root.right = bin_tree_from_array(arr , root.right , 2*i+2 , n)
        
        
        return root
    
    
l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
root = None
n1 = bin_tree_from_array(l1 , root , 0 , len(l1))

binary_tree_height(n1)