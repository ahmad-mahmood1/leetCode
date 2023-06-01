# https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab


def countLeafNodes(root, count=0):
    if not root:
        return count

    newCount = countLeafNodes(root.left, count)

    if not root.left and not root.right:
        newCount += 1
        
    newCount = countLeafNodes(root.right, newCount)

    return newCount
