# 数组中出现次数超过一半的数字 难度：简单
# 
"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例
    输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
    输出: 2
限制：
    1 <= 数组长度 <= 50000
"""

# 方法：排序取中位数即众数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]

# 方法：摩尔投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x