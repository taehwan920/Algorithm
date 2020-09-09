from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = deque([[0, root]])

        result = []

        while q:
            depth, now = q.popleft()
            if now.left == None and now.right == None:
                result.append([depth, now.val])
            for node in [now.left, now.right]:
                if node != None:
                    q.append([depth + 1, node])

        deepest = max(result, key=lambda x: x[0])[0]

        answer = 0
        for node in result:
            if node[0] == deepest:
                answer += node[1]

        return answer
