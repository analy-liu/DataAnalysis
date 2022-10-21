#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
示例：
    输入：root = [1,null,2,3]
    输出：[1,3,2]
提示：
    树中节点数目在范围 [0, 100] 内
    -100 <= Node.val <= 100
进阶：
    递归算法很简单，你可以通过迭代算法完成吗？
"""

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        def midtree(root):
            if not root: return None
            midtree(root.left)
            answer.append(root.val)
            midtree(root.right)
        midtree(root)
        return answer
# @lc code=end

