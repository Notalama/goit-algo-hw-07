class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def tree_sum(root):
    if root is None:
        return 0
    else:
        return root.data + tree_sum(root.left) + tree_sum(root.right)

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

total_sum = tree_sum(root)
print("Сума всіх значень у дереві:", total_sum)  # Виведе 350