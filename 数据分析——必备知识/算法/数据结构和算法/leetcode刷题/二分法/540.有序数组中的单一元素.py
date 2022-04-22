#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素 难度：Medium
#
"""
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

示例 1:

输入: [1,1,2,3,3,4,4,8,8]
输出: 2
示例 2:

输入: [3,3,7,7,10,11,11]
输出: 10
注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。
"""
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right)>>1
            if nums[mid] == nums[mid-1]:
                if mid & 1 == 1:
                    # 偶数
                    left = mid + 1
                else:# 奇数
                    right = mid -2
            elif nums[mid] == nums[mid+1]:
                if mid & 1 == 1:# 偶数
                    right = mid - 1
                else:# 奇数
                    left = mid +2
            else:
                return nums[mid]
        return nums[left]
"""
# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1 : return nums[0]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right)>>1
            if nums[mid] == nums[mid+1]: mid += 1
            if nums[mid] != nums[mid-1]: return nums[mid]
            if mid & 1 == 1:# 偶数
                left = mid +1
            else:# 奇数
                right = mid - 2
        return nums[left]
# @lc code=end

"""
左等单数，右变中-2
左等双数，左变中+1
右等单数，左变中+2
右等双数，右变中-1
"""