from tree import BinarySearchTree

def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.value

bst = BinarySearchTree()
bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(8)
bst.insert(12)
bst.insert(18)
bst.insert(3)

print("Найбільше значення:", find_max(bst.root))
