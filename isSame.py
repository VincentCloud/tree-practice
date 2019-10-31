import tree_node


class Solution:
    def isSameTree(self, p: tree_node, q: tree_node) -> bool:
        if p and not q or q and not p:
            return False
        elif not p and not q:
            return True
        if not p.left and not p.right and not q.left and not q.right:
            if p.val == q.val:
                return True
            else:
                return False
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False


if __name__ == "__main__":
    p = tree_node(1)
    p.left = tree_node(2)
    p.right = None
    q = tree_node(1)
    q.left = None
    q.right = tree_node(2)
    s = Solution()
    print(s.isSameTree(p, q))
