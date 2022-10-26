#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# Category	Difficulty	Likes	Dislikes
# algorithms	Easy (59.35%)	1538	-
# Tags
# Companies
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

 

# 说明:

# 为什么返回数值是整数，但输出的答案是数组呢?

# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

# 你可以想象内部操作如下:

# // nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
# int len = removeElement(nums, val);

# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
 

# 示例 1：

# 输入：nums = [3,2,2,3], val = 3
# 输出：2, nums = [2,2]
# 解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
# 示例 2：

# 输入：nums = [0,1,2,2,3,0,4,2], val = 2
# 输出：5, nums = [0,1,4,0,3]
# 解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
 

# 提示：

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100


# 左右指针
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0 # 左指针
        r = len(nums)-1 # 右指针
        while r>=0 and nums[r] == val: # 使右指针移动到非目标元素位置
            r -= 1
        while l<r:  # 当左右指针重合时，遍历完成
            if nums[l] == val:
                nums[l] = nums[r] # 当左指针遇到目标元素，将左指针赋值为右指针
                r -= 1 # 当前右指针元素已使用，向左移动一格
                while nums[r] == val: # 然后继续将右指针移动到非目标元素位置，防止连续出现目标元素
                    r -= 1
            l += 1 # 无论是否交换，左指针+1
        return r+1    
# @lc code=end

# 快速开发，实现功能
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while 1:
            try:
                nums.remove(val)
            except:
                return len(nums)

# 快慢指针
class Solution:
    def removeElement(self, nums, val) -> int:
        slow = 0 # 定义慢指针
        for fast in range(len(nums)):# 快指针遍历完数组
            if nums[fast] !=val:# 当快指针不等于目标元素时，慢指针取快指针的元素并+1，形成快慢差，最后快指针跑完了，慢指针比快指针少了目标元素的个数
                nums[slow] = nums[fast]
                slow +=1
        return slow

# 解法：双指针