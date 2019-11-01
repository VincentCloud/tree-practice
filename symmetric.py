from tree_node import TreeNode
from list_to_tree import ConvertTree
from traversal import Traversal

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            t = Traversal()
            ll = t.in_order(root.left)
            lr = t.in_order_right(root.right)
            if ll == lr:
                return True
            else:
                return False

if __name__ == "__main__":
    sample = "[5,4,1,null,1,null,4,2,null,2,null]"
    c = ConvertTree()
    root = ConvertTree.convert_tree(c, sample)
    s = Solution()
    print(Solution.isSymmetric(s, root))
