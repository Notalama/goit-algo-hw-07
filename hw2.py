class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_minimum_value(root):
    if root is None:
        return None  # Порожнє дерево

    current = root
    while current.left is not None:
        current = current.left
    return current.data

# Приклад використання
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

min_value = find_minimum_value(root)
print("Найменше значення у дереві:", min_value)  # Виведе 20