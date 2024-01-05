class Tree:

    def __init__(self):
        self.head = None
        self.left = None
        self.right = None
        self.size = 0

def tree_add(L, value):
    if L is None:
        L = Tree()
    
    if L.head is None:
        L.head = value
        L.size = 1
    elif L.head == value:
        pass
    elif L.head < value:
        if L.right is None:
            L.right = Tree()
        tree_add(L.right, value)
    else:
        if L.left is None:
            L.left = Tree()
        tree_add(L.left, value)
    
    if L.right is None and L.left is None:
        L.size = 0 if L.head is None else 1
    elif L.right is None:
        L.size = L.left.size + 1
    elif L.left is None:
        L.size = L.right.size + 1
    else:
        L.size = max(L.left.size, L.right.size) + 1


L = Tree()

for i in map(int, input().split()):
    tree_add(L, i)

print(L.size)