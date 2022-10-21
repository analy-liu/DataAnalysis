#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组 难度：easy
#
"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

 

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
 

提示：

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109
"""
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        while j < n and i < j+m:
            if nums1[i] <= nums2[j] and nums2 != 0:
                i += 1
            else:
                nums1[]
                for back in range(n+m-1, i, -1):
                    nums1[back] = nums1[back-1]
                nums1[i] = nums2[j]
                j += 1
        if j < n:
            nums1[i:] = nums2[j:]
"""
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        pos = n+m-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[pos] = nums1[i]
                i -= 1
            else:
                nums1[pos] = nums2[j]
                j -= 1
            pos -= 1
        if i == -1:
            nums1[0:pos+1] = nums2[0:pos+1]
"""
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        pos = n+m-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[pos] = nums1[i]
                i -= 1
            else:
                nums1[pos] = nums2[j]
                j -= 1
            pos -= 1
        if i == -1:
            nums1[0:pos+1] = nums2[0:pos+1]
        
# @lc code=end