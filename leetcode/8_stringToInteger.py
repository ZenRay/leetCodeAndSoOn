#coding:utf8
"""
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

提示：

本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
 

示例 1:

输入: "42"
输出: 42
示例 2:

输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
     因此返回 INT_MIN (−231) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-to-integer-atoi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import re
import string

maxLimitation = 0x7fffffff
minLimitation = -0x80000000


class Solution1:
    def myAtoi(self, string: str) -> int:
        pattern = re.compile(r"^([\-\+]?\d+)|(?:^ +)([\-\+]?\d+)")
        maxLimitation = 0x7fffffff
        minLimitation = -0x80000000

        try:
            groups = pattern.search(string).groups()
            result = groups[0] or groups[1]
            
            result = int(result)
        # 不能匹配结果是 None，使用 groups 方法会报错
        except AttributeError:
            result = 0
        
        if result > maxLimitation:
            return maxLimitation
        elif result < minLimitation:
            return minLimitation
        else:
            return result

        """
        在讨论区，看见单行解决问题的方式：本质上是一样的，差异是先清除左侧的空格和列表解析，这样直接简化了正则
        class Solution:
            def myAtoi(self, s: str) -> int:
                return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

        作者：QQqun902025048
        链接：https://leetcode-cn.com/problems/string-to-integer-atoi/solution/python-1xing-zheng-ze-biao-da-shi-by-knifezhu/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """



class Solution2:
    """
    参考了用 C++ 代码，运行速度和空间消耗忽略不计的方案， Python 方式效率上有提高
    （时间上比直接用正则提高了 10 ms），但没有 C++ 明显。
    解题思路：直接判断当前字符是否为数字，并不断递增索引位置；该方式存在缺陷是不能推广，
    假设需要解决字符间数字时会不能提取数字：
    class Solution {
    public:
        int myAtoi(string str) {
            int i = 0, flag = 1;
            long res = 0; //默认flag = 1，正数
            while (str[i] == ' ') i ++; //若str全为空格，str[i] = '\0'(最后一个i)
            if (str[i] == '-') flag = -1;
            if (str[i] == '-' || str[i] == '+') i ++;
            for (; i < str.size() && isdigit(str[i]); i ++)  {
                res = res * 10 + (str[i] - '0');
                if (res >= INT_MAX && flag == 1) return  INT_MAX;
                if (res > INT_MAX && flag == -1) return  INT_MIN;
            } 
            return flag * res;
        }
    };

    作者：OrangeMan
    链接：https://leetcode-cn.com/problems/string-to-integer-atoi/solution/cjian-dan-dai-ma-shuang-bai-by-orange-32-2/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """
    def myAtoi(self, text: str) -> int:
        number = "0"
        currentIndex = 0
        text = text.lstrip()    # 清除左侧空格
        
        # 判断首个符号的情况
        if text[currentIndex] == "-":
            flag = -1
            currentIndex += 1
        elif text[currentIndex] == "+":
            flag = 1
            currentIndex += 1
        else:
            flag = 1

        # 判断是否为字符并且不断递增索引
        while currentIndex < len(text) and text[currentIndex].isdigit():
            number += text[currentIndex]
            currentIndex += 1

        result = int(number) * flag

        if result > maxLimitation:
            return maxLimitation
        elif result < minLimitation:
            return minLimitation
        else:
            return result

        
            
class Solution3:
    """
    DFA 有限状态机的思路：
    ![](https://assets.leetcode-cn.com/solution-static/8_fig1.PNG)
    1. 起位是 start，下一位是 " " 时 状态是 start, 这样可以不断在本位上更新
    2. 起始是 start，下一位是 "-" 或者 "+" 时，状态更新为 signed
    3. 起始是 signed，仅有在下一位是数字字符时，状态更新为 number
    4. 起始是 number，仅有下一位是数字字符时，状态更新为 number
    5. 起始是 start，下一位是数字字符时，状态更新为 number
    6. 其他情况下，更新为 end

    作者：LeetCode-Solution
    
    链接：https://leetcode-cn.com/problems/string-to-integer-atoi/solution/zi-fu-chuan-zhuan-huan-zheng-shu-atoi-by-leetcode-/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """
    def myAtoi(self, string: str) -> int:
        automation = Automation() 

        for char in string:
            automation.update(char)

            # 增加条件判断，在终止时停止，减少时间消耗
            if automation.currentState == "END":
                break

        # 解析结果
        result = automation.sign * int(automation.value)

        return min(result, maxLimitation) if automation.sign == 1 else max(result, minLimitation)
        




class Automation:
    def __init__(self):
        self.currentState = "START"
        self.sign = 1
        self.value = "0"
        
        # 所有字符顺序，因为其他情况全是非数字字符，最后一个直接排除得到结果
        self.charOrder = [" ", "+-", string.digits]
        # 状态转换表
        self.table = {
                    # " ", "+-", "0-9", other
            "START": ["START", "SIGN", "NUMBER", "END"],
            "SIGN": ["END", "END", "NUMBER", "END"], 
            "NUMBER": ["END", "END", "NUMBER", "END"],
            "END": ["END", "END", "END", "END"]
        }



    def update(self, char):
        # 获取 char 所在的 charOrder 顺序，如果是非 0-9-+ 和空格，那么是没有 1，直接得到索引值为 3
        indexes = [1 if char in stands else 0 for stands in self.charOrder]
        index = indexes.index(1) if 1 in indexes else 3
        
        # 更新状态、数据值或者符号
        self.currentState = self.table[self.currentState][index]
        if self.currentState == "NUMBER":
            self.value += char
        elif self.currentState == "SIGN":
            self.sign = -1 if char == "-" else 1

        

if __name__ == "__main__":
    text =  "-4193 with words" # "-983472332" # "words and 987" # 
    t = Solution3()
    print(t.myAtoi(text))