# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = None


class Solution:
    def build_tree(self, root, element):
        if not root:
            root = TreeNode()
            root.val = element
            return root

        if element > root.val:
            root.right = self.build_tree(root.right, element)

        else:
            root.left = self.build_tree(root.left, element)

        return root

    def bst_from_preorder(self, preorder) -> TreeNode:
        global root
        for ele in preorder:
            self.build_tree(root, ele)

        return root


if __name__ == "__main__":
    s = Solution()
    print(s.bst_from_preorder([8, 5, 1, 7, 10, 12]))
