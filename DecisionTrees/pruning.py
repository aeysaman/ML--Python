from objects import Node, Tree


def pruneTree(tree):
    prune(tree.top)

def prune(node):
    prune(node.left)
    prune(node.right)

    




