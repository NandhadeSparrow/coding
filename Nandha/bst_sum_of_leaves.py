class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def sum_of_leaves(self):
        return self._sum_of_leaves(self.root)

    def _sum_of_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.key
        return self._sum_of_leaves(node.left) + self._sum_of_leaves(node.right)

# Example usage
numbers = list(map(int,input().split()))

bst = BST()
for number in numbers:
    bst.insert(number)

sum_leaves = bst.sum_of_leaves()
print("Sum of leaf nodes:", sum_leaves)
