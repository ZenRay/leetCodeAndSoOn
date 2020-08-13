#coding:utf8
"""
给定一个字符串，逐个翻转字符串中的每个单词。

 

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

进阶：

请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def reverseWords(self, s: str) -> int:
        """
        依赖 str 特性计算：
        1. 排除掉两侧空格
        2. 中间是空格的时候，得到前一个单词，继续遍历后面字符串
        """
        s = s.strip()
        # 如果是空字符，直接返回 0
        if len(s) == 0:
            return ""
        
        result = []
        char = ""
        while s:
            if s[0] == " ":
                if char:
                    result.insert(0, char)
                char = ""
            else:
                char += s[0]

            s = s[1:]
        
        # 添加最后一个 char
        if char:
            result.insert(0, char)
        
        return " ".join(result)


class Solution1:
    def clear_space(self, word):
        """清除空格
        """
        left = 0
        right = len(word)
        while left < right:
            # 如果左右两侧都不是空格时停止
            if word[left] != " " and word[right - 1] != " ":
                break
            if word[left] == " ":
                left += 1
            
            if word[right] == " ":
                right -= 1
        
        return word[left:right]

    
    def reverseWords(self, s):
        """
        不依赖 Python 的 str 特性完成：
        从右侧向左侧移动，遇到空格则作为一个字符串处理之后给到结果至列表中
        """
        start = 0
        right = len(s) - 1

        char = ""
        result = []
        while right >= start:
            if s[right] == " ":
                word = self.clear_space(char)
                if word:
                    result.append(word)
                char = ""
            else:
                char = s[right] + char

            # 移动右指针
            right -= 1
        else:
            if self.clear_space(char):
                result.append(self.clear_space(char))
        
        
        return " ".join(result)






if __name__ == "__main__":
    text = "  hello world!  "#  "the sky is blue"
    s = Solution1()
    print(s.reverseWords(text))