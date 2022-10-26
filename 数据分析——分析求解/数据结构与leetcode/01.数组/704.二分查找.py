#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
# """
# Category	Difficulty	Likes	Dislikes
# algorithms	Easy (54.53%)	1021	-
# Tags
# Companies
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


# 示例 1:

# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 示例 2:

# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
 

# 提示：

# 你可以假设 nums 中的所有元素是不重复的。
# n 将在 [1, 10000]之间。
# nums 的每个元素都将在 [-9999, 9999]之间。
# """

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)-1 # 定义target在左闭右闭的区间里，[left, right]
        l = 0
        while l<=r: # 当left==right，区间[left, right]依然有效，所以用 <=
            m = (l+r)//2
            if nums[m] < target:
                l = m+1 # target 在右区间，所以[middle + 1, right]
            elif nums[m] > target:
                r = m-1 # target 在左区间，所以[left, middle - 1]
            else:
                return m # 数组中找到目标值，直接返回下标
        return -1 # 未找到目标值

# @lc code=end

# 关键点：二分法
# 在while处，确定区间左右是闭还是开，然后决定下面下标是否+1-1