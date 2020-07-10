#coding:utf8
"""

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
https://leetcode-cn.com/problems/longest-common-prefix/
"""
import numpy as np

class Solution:
    """
    思路：
    暴力比较，直接遍历数据。通过最小字符串和最大字符串比较：
    1. 因为是需要考虑到前缀，因此直接使用 min 和 max 获取到 ASCII 码下最小顺序字符串和最大的
        顺序字符串
    2. 比较最大和最下之间是否存在相同的前缀字符串
    3. 最后在检验一次公共前缀字串是否都存在
    """
    def longestCommonPrefix(self, strs) -> str:
        # 过滤空序列
        if len(strs) < 1:
            return ""

        keep_char = "" # 保留的字串
        min_char = min(strs)
        max_char = max(strs)

        for index, char in enumerate(min_char):
            if char == max_char[index]:
                keep_char += char
            else:
                break
        
        return keep_char if all([keep_char in d for d in strs]) else ""


class Solution1:
    """
    暴力破解第二种思路:
    公共前缀字串，肯定是由最短字串的前缀字串确定的：
    1. 确认最短字串
    2. 扫描最短字串的字符，和其他字串存在公共字符即是公共前缀
    扫描时间比上一个短大约 30ms
    """
    def longestCommonPrefix(self, strs) -> str:
        # 过滤空序列
        if len(strs) < 1:
            return ""
        result = ""
        # 获取最小长度字符串索引
        min_index = np.argmin([len(i) for i in strs])
        source = strs[min_index]
        targets = [char for index, char in enumerate(strs) if index != min_index]
        for index, char in enumerate(source):
            if all([char == target[index] for target in targets]):
                result += char
            else:
                break
            
        return result



if __name__ == "__main__":
    chars =  [""] #["ca", "a"] #["flower","flow","flight"] # ["dog","racecar","car"] #
    t = Solution1()
    print(t.longestCommonPrefix(chars))