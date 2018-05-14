class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

def lowestCommonAncestor(n1, n2, root):
    node = root
    parent = None
    if n1.value < n2.value:
        left, right = n1, n2
    else:
        left, right = n2, n1
    while True:
        if node.value < left.value:
            parent = node
            node = node.right
        elif node.value > right.value:
            parent = node
            node = node.left
        elif node.value == left.value or node.value == right.value:
            return parent
        else:
            return node


if __name__ == '__main__':
    n1 = Node(5)
    n2 = Node(3)
    n3 = Node(7)
    n4 = Node(2)
    n5 = Node(4)
    n6 = Node(6)
    n7 = Node(8)
    n8 = Node(1)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8

    print(lowestCommonAncestor(n8, n5, n1))
    print(lowestCommonAncestor(n6, n7, n1))
    print(lowestCommonAncestor(n8, n3, n1))
    print(lowestCommonAncestor(n4, n2, n1))
    print(lowestCommonAncestor(n5, n1, n1))