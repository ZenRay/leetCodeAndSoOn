#coding:utf8
"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np

class Solution1:
    def longestPalindrome(self, s: str) -> str:
        high = len(s) - 1
        current = 0
        offset = 0
        string = ""
        palindrome = ""
        checked_char = set()
        while current <= high:
            string = s[current]
            mid = s[current+1:]
            if s[current] in checked_char:
                continue

            checked_char.add(s[current])
            while s[current] in mid:
                offset = mid.index(s[current])
                string += mid[:offset+1]
                mid = s[offset+1:]

            # temp = self.check(string) or 
            if len(temp) > len(palindrome) and temp == temp[::-1]:
                palindrome = temp      
                

            # 目前的思路是全部字符串检查，但是时间复杂度受限，
            # temp = self.check(string)
            # if len(temp) > len(palindrome) and temp == temp[::-1]:
            #     palindrome = temp            
            
            current += 1
        
        return palindrome


    def check(self, x):
        if x == x[::-1]:
            return x
        elif len(x) == 1:
            return ""
        return self.check(x[::-1]) or self.check(x[1:])
        # while len(x) > 1:
        #     if x == x[::-1]:
        #         return x
        #     else:
        #         x = x[1:]
        # return result


class Solution2:
    # 在解题中需要解决其中的最大长度和最大长度的起始索引位置即可，在最终结果中获取最终答案
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        
        maxLength = 0
        start = 0
        for left in range(len(s) - 1):
            right = left + 1
            while right < len(s):
                if right - left + 1 > maxLength and self.validPalindromic(s, left, right):
                    maxLength = right - left + 1
                    start = left
                right += 1
        return s[start: maxLength ]
    

    def validPalindromic(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

        else:
            return True


class Solution3:
    # 使用动态规划求解
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        # 创建动态规划表
        array = np.zeros((len(s), len(s)))

        # 显性的将对角线设置为 1
        for i in range(len(s)):
            array[i, i] = 1 

        start = 0
        maxLength = 0

        for column in range(1, len(s)):
            # 只需要遍历半角即可，因此行的遍历最大长度为列位置
            for row in range(column):
                # 如果首尾不相等，那么必定不是回文序列，因此设置结果为 False
                if s[column] != s[row]:
                    array[row, column] = False
                # 首尾相等，且在去掉首尾只有一个字符或者没有字符时必定是回文
                elif s[row] == s[column] and (column - row) < 3:
                    array[row, column] = True
                # 首尾相等，但字符长度超过 3，表明去掉首尾之后是否为回文字符串，由其子串决定
                elif s[column] == s[row] and column - row >= 3:
                    array[row, column] = array[row+1, column-1]

                if array[row, column] and column - row + 1 > maxLength:
                    maxLength = column - row + 1
                    begin = row

        return s[begin: begin + maxLength]


class Solution4:
    # 中心扩散法
    def longestPalindrome(self, string):
        # 存在从中间字符向两侧寻找回文和，从中间点两侧两个字符向两侧找的情况——也就是说存在字符 
        # 是偶数和奇数的情况

        # 首先判断情况一，如果是字符长度小于 3，那么直接返回就可以了
        if len(string) < 2:
            return string
        
        # 初始化需要的变量：字符串起始索引和回文长度
        start = 0
        maxLength = 0

        # 为了方便能够有扩散的基础，因此从第二个字符作为开始
        #  TODO： 待验证：同理最后一个字符也没有向两侧扩散基础，因此结束位置为长度减一
        for index in range(1, len(string)):
            # 奇数情况下，左右两边起始都是以中心字符
            oddResult = self.Condition(string, index, index)
            # 偶数情况下，左右两边的起始是前一个字符和当前字符确认
            evenResult = self.Condition(string, index - 1, index)

            # 因为字符长度存在奇偶数差异，扩散结果存在差异，即最大长度计算方式存在差异
            # 1. 奇数情况下，直接加上当前索引位置上的字符个数（1） 即可.如下图
            # []|[index]|[]
            # if oddResult > 0:
            oddLength = oddResult * 2 + 1
            # else:
            #     oddLength = 0

            # 2. 偶数情况下，需要加两个字符个数，但是需要如果如果当前两个索引上的字符不是回文
            # 得到的结果是 0，因此是否加 2 需要通过结果判断。原因如下图：
            # []|[index-1]|[index]|[]
            # 需要注意偶数情况下，可能只更新一次，所以结果是 0 表示满足结果
            if evenResult >= 0:
                evenLength = evenResult * 2 + 2
            else:
                evenLength = 0
            
            # 最后判断所有结果上是不是大于最大长度，判断是否需要记录结果
            if oddLength >= maxLength:
                maxLength = oddLength
                start = index - oddResult # 当前所有减去奇数情况下的半长度就是起始索引
            
            if evenLength > maxLength:
                maxLength = evenLength
                start = index - evenResult - 1  # 当前索引减去偶数情况下的半长度和前一个位置就是起始索引
            

        return string[start: start + maxLength]




    def Condition(self, string, left, right):
        # 主要计算向两侧扩散的结果，在满足 left 和 right 索引时 left 更新向左侧移动而 
        # right 向右侧移动，同时计数移动了几次那么可以求得最大长度的半长度
        halfMaxLegth = -1

        while left >= 0 and right < len(string):
            if  string[left] == string[right]:
                left -= 1
                right += 1
                halfMaxLegth += 1
            else:
                break
        
        return halfMaxLegth



if __name__ == "__main__":
    string = "ac" #"cbbd" #"ababad"
    s = Solution4()
    print(s.longestPalindrome(string))