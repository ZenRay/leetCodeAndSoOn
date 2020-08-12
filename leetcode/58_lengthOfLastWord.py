#coding:utf8
"""
58. 最后一个单词的长度
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

 

示例:

输入: "Hello World"
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        不依赖 str 特性计算：
        1. 排除掉两侧空格
        2. 中间是空格的时候，得到前一个单词，继续遍历后面字符串
        """
        while s[0] == " ":
            s = s[1:]
        
        while s[-1] == " ":
            s = s[:-1]
        
        # 如果是空字符，直接返回 0
        if len(s) == 0:
            return 0
        

        char = ""
        while s:
            if s[0] == " ":
                char = ""
            else:
                char += s[0]

            s = s[1:]
        
        return len(char)


class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        """
        完全以来 str 的行管方法处理，使用去空格和空格拆分之后得到最后一个单词，计算长度
        """
        if len(s.strip()) == 0:
            return 0
        
        return len(s.split()[-1])

if __name__ == "__main__":
    s = "Today is a nice day" # "hello "
    t = Solution1()
    print(t.lengthOfLastWord(s))