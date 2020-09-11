class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


""" 
The function Compute the "height" of a tree. Height is the  
number f nodes along the longest path from the root node  
down to the farthest leaf node. 
"""


def height(node):
    # Base Case : Tree is empty
    if node is None:
        return 0

        # If tree is not empty then height = 1 + max of left
    # height and right heights
    return 1 + max(height(node.left), height(node.right))


# Function to get the diameter of a binary tree
def diameter(root):
    # Base Case when tree is empty
    if root is None:
        return 0

        # Get the height of left and right sub-trees
    l_height = height(root.left)
    r_height = height(root.right)

    # Get the diameter of left and right sub-trees
    l_diameter = diameter(root.left)
    r_diameter = diameter(root.right)

    # Return max of the following tree:
    # 1) Diameter of left subtree
    # 2) Diameter of right subtree
    # 3) Height of left subtree + height of right subtree +1
    return max(l_height + r_height + 1, max(l_diameter, r_diameter))


# Driver program to test above functions

""" 
Constructed binary tree is  
            1 
          /   \ 
        2      3 
      /  \ 
    4     5 
"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Diameter of given binary tree is %d" % (diameter(root)))
print("Height of btree is %d" % (height(root)))
