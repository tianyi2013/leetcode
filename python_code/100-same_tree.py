class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_same_tree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    def flattern_tree(tree, array):
        if not tree:
            return array
        array.append(tree.val)
        if tree.left:
            flattern_tree(tree.left, array)
        else:
            array.append('null')
        if tree.right:
            flattern_tree(tree.right, array)
        else:
            array.append('null')
        return array

    return flattern_tree(p, []) == flattern_tree(q, [])

