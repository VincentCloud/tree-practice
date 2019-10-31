import tree_node
from list_to_tree import Convert


class Solution:
    def isSymmetric(self, root: tree_node) -> bool:
        l = self.in_order(root)
        i = 0
        j = len(l) - 1

        while i < j and i < len(l):
            if l[i] != l[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

    def in_order(self, root: tree_node):
        if not root:
            return [None]
        elif not root.left and not root.right:
            return [root.val]
        else:
            return self.in_order(root.left) + [root.val] + self.in_order(root.right)


if __name__ == "__main__":
    sample = [5, 4, 1, None, 1, None, 4, 2, None, 2, None]
    i = 0
    j = len(sample)
    root = None
    c = Convert()
    root = c.list_to_tree(sample, root, i, j)
    print(c.in_order(root))

    s = Solution()
    result_list = s.in_order(root)
    print(result_list)
    print(s.is_symmetric(root))
