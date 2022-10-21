#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置 难度：Medium
#
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
"""
"""初始想法
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []: return [-1, -1]
        r = len(nums)-1
        l = 0
        while (nums[r] != target or nums[l] != target) and l != r:
            mid = (l + r)>>1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid+1
        if l == r and nums[r] != target:
            return [-1, -1]
        while r <= len(nums)-1 and nums[r] == target:
            r += 1
        return [l, r-1]
"""
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size == 0: return[-1, -1]
        left = self.__search_left(nums, target, size)
        if left == -1:
            return [-1, -1]
        right = self.__search_right(nums, target, size)
        return [left, right]
    def __search_left(self, nums, target, size):
        left = 0
        right = size - 1
        while left < right:
            mid = (left + right)>>1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid +1
        if nums[left] == target:
            return left
        else:
            return -1
    def __search_right(self, nums, target, size):
        left = 0
        right = size - 1
        while left < right:
            mid = (left + right + 1)>>1
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        return right
# @lc code=end

