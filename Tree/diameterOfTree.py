# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab


def diameterFast(root):
    if not root:
        return 0, 0

    leftDiameter, leftHeight = diameterFast(root.left)
    rightDiameter, rightHeight = diameterFast(root.right)

    diameterCombined = max(
        [leftDiameter, rightDiameter, leftHeight + rightHeight + 1]
    )

    return diameterCombined, max(leftHeight , rightHeight) + 1


