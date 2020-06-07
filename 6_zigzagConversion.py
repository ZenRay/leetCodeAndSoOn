#coding:utf8
"""
6. Z 字形变换


将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""
from __future__ import absolute_import

import numpy as np

class Solution1:
    """
    思路：
        因为不需要考虑添加空字符来格式化输出，那么直接通过控制向下之后在反向一次，
        作为单一一个批次字符，那么通过 zip 进行匹配上需要的批次索引和字符串索引
        就可以得到 numRows 长度的 list
    """
    def convert(self, string, numRows):
        # 创建需要数量的 list 以存储字符
        result = ["" for _ in range(numRows)]

        # 需要考虑 numRows 中的长度，如果长度为 1 时，直接每次取结果中最后一个索引即可
        # 如果是大于 1，那么考虑 numRows 需要的长度和去掉头尾之后的长度作为 unit，计算出
        # 需要的索引——向上取整的方式
        if numRows > 1:
            reverseIndexes = [i * -1 for i in range(2, numRows)]
            rowIndexes = (list(range(numRows)) + reverseIndexes) * \
                    int(np.ceil(len(string) / (numRows * 2 - 2)))
        elif numRows == 1:
            rowIndexes = [-1] * len(string)
        
        # 字符串索引和 result 中需要的行索引匹配
        for index, rowIndex in zip(range(len(string)), rowIndexes):
            result[rowIndex] += string[index]

        return "".join(result)


    def convert1(self, string, numRows):
        result = []
        stored = []
        prevIndex = 0
        currentIndex = 0
        offset = numRows * 2 - 2

        # import ipdb; ipdb.set_trace()
        for index in range(numRows):
            currentIndex = index
            temp = []
            midColumn = 0
            while currentIndex < len(string) or currentIndex not in stored:
                stored.append(currentIndex)
                
                if currentIndex + offset < len(string):
                    if currentIndex % (numRows - 1) == 0:
                        temp += ([string[currentIndex]] + [""] * (numRows - 2))
                    else:
                        temp += ([string[currentIndex]] +  [""] * (offset - index * 2 - 2 - index % 2) + [string[currentIndex + offset - index * 2]]+ [""] * (index - 1) )
                        stored.append(currentIndex + offset - index * 2)
                    currentIndex += offset
                else:
                    temp.append(string[currentIndex])
                    midRow = currentIndex
                    result.append(temp)
                    break
            
        return result

if __name__ == "__main__":
    from pprint import pprint
    string = "PAYPALISHIRING"# "123456789ABCDEFG" #"LEETCODEISHIRING"
             
    t = Solution1()
    pprint(t.convert(string, 2))

"PINALSIGYAHPI"
"PINALSIGYAHRPI"