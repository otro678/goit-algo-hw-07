from tree import BinarySearchTree

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.value

bst = BinarySearchTree()
bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(8)
bst.insert(12)
bst.insert(18)
bst.insert(3)

print("Найменше значення в дереві:", find_min(bst.root))
