# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.val:
            return []
        result = []
        q = [[root, []]]
        while q:
            now, arr = q.pop(0)
            arr.append(str(now.val))
            if now.left == None and now.right == None:
                result.append(arr)
            for node in [now.left, now.right]:
                if node != None:
                    q.append([node, arr[:]])

        result = list(map(lambda x: '->'.join(x), result))
        return result
