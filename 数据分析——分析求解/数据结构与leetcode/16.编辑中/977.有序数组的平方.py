#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1
        ans = [-1]*n
        while l<r:
            if abs(nums[l])<abs(nums[r]):
                

                
# @lc code=end