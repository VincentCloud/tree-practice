from tree_node import TreeNode


class Traversal:
    def in_order(self, root):
        if root is None:
            return [None]
        elif not root.left and not root.right:
            return [root.val]
        else:
            return self.in_order(root.left) + [root.val] + self.in_order(root.right)

    def in_order_right(self, root):
        if root is None:
            return [None]
        elif not root.left and not root.right:
            return [root.val]
        else:
            return self.in_order(root.right) + [root.val] + self.in_order(root.left)