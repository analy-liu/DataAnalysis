# 数组中的逆序对
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
"""
示例
输入: [7,5,6,4]
输出: 5
"""

# 方法：归并排序
class Solution(object):
    def reversePairs(nums):
        if len(nums) == 1:
            return 0
        else:
            num = 0 #逆序对
            member = 2 #每组成员数，最少二人一组
            LenArr = len(nums)
            while LenArr>member/2:
                member_sort = []
                """单组成员数大于一半时停下,log(n/2)"""
                for n in range(0, LenArr, member):
                    """i为每组成员的第一个，for+while循环加起来为2/n"""
                    mid = member//2 #成员二分
                    i = n
                    j = n+mid
                    if j >= LenArr :
                        for i in range(n, LenArr):
                            member_sort.append(nums[i])
                        break
                    j_edge = n+member if n+member <= LenArr else LenArr
                    while i < n+mid and j < j_edge:
                        if nums[i] <= nums[j]:
                            member_sort.append(nums[i])
                            i += 1
                            num += j-n-mid
                        else:
                            member_sort.append(nums[j])
                            j += 1
                    if j == j_edge:
                        while i < n+mid:
                            member_sort.append(nums[i])
                            i += 1
                            num += j_edge-n-mid
                    else:
                        while j < j_edge:
                            member_sort.append(nums[j])
                            j += 1
                nums = member_sort
                member = member*2
        return nums, num

if __name__ == "__main__":
    List = [1,3,2,3,1,3]
    List, num = Solution.reversePairs(List)
    print(List, num)