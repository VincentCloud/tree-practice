from tree_node import TreeNode
import traversal


class ConvertTree:
    def convert_tree(self, input):
        input = input.strip()
        input = input[1:-1]
        if not input:
            return None

        inputValues = [s.strip() for s in input.split(',')]
        root = TreeNode(int(inputValues[0]))
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(inputValues):
            node = nodeQueue[front]
            front = front + 1

            item = inputValues[index]
            index = index + 1
            if item != "null":
                leftNumber = int(item)
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)

            if index >= len(inputValues):
                break

            item = inputValues[index]
            index = index + 1
            if item != "null":
                rightNumber = int(item)
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)
        return root
if __name__ == "__main__":
    sample = '[5,4,1,null,1,null,4,2,null,2,null]'
    t = traversal.Traversal()
    c = ConvertTree()
    sample_tree = c.convert_tree(sample)
    print(t.in_order(sample_tree))




