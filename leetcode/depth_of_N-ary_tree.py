class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        deepest = 1
        while stack:
            now_node, now_dep = stack.pop()
            if now_dep > deepest:
                deepest = now_dep
            if not now_node:
                continue
            for node in now_node.children:
                if node:
                    stack.append([node, now_dep + 1])

        return deepest
