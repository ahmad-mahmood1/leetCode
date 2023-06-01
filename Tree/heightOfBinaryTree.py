# https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab


def heightOfTree(root, height=0):
    if not root:
        return 0

    leftH = heightOfTree(root.left, height)
    rightH = heightOfTree(root.right, height)

    return max(leftH, rightH) + 1
