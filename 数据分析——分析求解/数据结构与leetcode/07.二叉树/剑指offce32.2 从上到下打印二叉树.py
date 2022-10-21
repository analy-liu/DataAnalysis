# 从上到下打印二叉树 II 难度：简单
"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

示例：
给定二叉树: [3,9,20,null,null,15,7],
         3
        / \
       9  20
         /  \
        15   7
    返回
    [
    [3],
    [9,20],
    [15,7]
    ]
提示：
    节点总数 <= 1000
"""




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        answer = []
        temp_val = [root.val]
        temp_map = [root]
        while temp_map:
            answer.append(temp_val)
            temp_val = []
            temp_map_next = []
            for n in temp_map:
                if n.left:
                    temp_map_next.append(n.left)
                    temp_val.append(n.left.val)
                if n.right:
                    temp_map_next.append(n.right)
                    temp_val.append(n.right.val)
            temp_map = temp_map_next
        return answer