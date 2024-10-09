from tree import BinarySearchTree

def find_sum(node):
    if node is None:
        return 0
    return node.value + find_sum(node.left) + find_sum(node.right)

bst = BinarySearchTree()
bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(8)
bst.insert(12)
bst.insert(18)
bst.insert(3)

print("Сума всіх значень у дереві:", find_sum(bst.root))