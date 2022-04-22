#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词 难度：Medium
# 给定一个字符串，逐个翻转字符串中的每个单词。
"""
说明：

无空格字符构成一个 单词 。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
示例：
    输入："  hello world!  "
    输出："world! hello"
    解释：输入字符串可以在前面或者后面包含多余的空格，
    但是反转后的字符不能包括。
提示
    1 <= s.length <= 104
    s 包含英文大小写字母、数字和空格 ' '
    s 中 至少存在一个 单词
"""

# 方法一：使用正则表达式，比较绕
"""
import re
class Solution:
    def reverseWords(self, s: str) -> str:
        Match = re.compile(r"\w*\w")
        StrList = Match.findall(s)
        res = StrList[-1]
        for i in range(-2,-len(StrList)-1,-1):
            res += " " + StrList[i] 
        return res
"""
# 方法二：使用内置函数"split"与"join", 分割+倒序合并
# split:O(N) join:O(N)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        return (" ").join(s.split()[::-1])
"""
# 方法三：双指针遍历
##3.1 直接在字符串里添加,time 70% memory 20%
"""
class Solution:
def reverseWords(self, s: str) -> str:
    i = len(s)-1
    j = len(s)
    res = ""
    while i != -2:
        if s[i] == " " or i == -1:
            temp = s[i+1:j]
            if temp != "":
                res = "{}{}{}".format(res, temp , " ")
            j = i
        i -= 1
    return res[0:len(res)-1]
"""
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = ""
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res = "{}{}{}".format(res, s[i+1:j+1], " ") # 添加单词
            while s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
        return res[0:len(res)-1] # 拼接并返回
"""
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = ""
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res += s[i+1:j+1] + " " # 添加单词
            while s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
        return res[0:len(res)-1] # 拼接并返回
"""
##3.2 转化成列表再合并 time 30% memory 6%
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        i = len(s)-1
        j = len(s)
        res = []
        while i != -2:
            if s[i] == " " or i == -1:
                if i+1 != j:
                    res.append(s[i+1:j])
                j = i
            i -= 1
        return " ".join(res)
"""
"""最佳答案
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1]) # 添加单词
            while s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
        return ' '.join(res) # 拼接并返回
"""

# 提交内容
# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1]) # 添加单词
            while s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
        return ' '.join(res) # 拼接并返回
# @lc code=end

