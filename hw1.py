class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_maximum_value(root):
    if root is None:
        return None  # Порожнє дерево

    current = root
    while current.right is not None:
        current = current.right
    return current.data

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
# root.right.right = Node(80)

max_value = find_maximum_value(root)
print("Найбільше значення у дереві:", max_value)