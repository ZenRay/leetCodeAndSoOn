#coding:utf8
"""
13. 罗马数字转整数
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
mapping = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Node:
    def __init__(self, char):
        self.value = mapping[char]
        self.char = char
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, char):
        self.size += 1
        if self.head is None:
            self.head = Node(char)
        else:
            node = Node(char)
            node.next = self.head
            self.head = node
    
    def pop(self):
        if self.size == 0:
            return 0, ""
        self.size -= 1
        value = self.head.value
        char = self.head.char

        # 更新顶部数据
        self.head = self.head.next

        return (value, char)


class Solution:
    """
    思路：
    利用 Stack 先进后出对字符串进行排序，之后将头部数据比较大小得出结果
    """
    def romanToInt(self, string: str) -> int:
        sequence = Stack()
        for char in string:
            sequence.push(char)

        total_value, prev_char = sequence.pop()
        while True:
            current_value, current_char = sequence.pop()

            # 循环终止发生在数量为 0 时
            if current_value == 0:
                break

            # 判断字符大小确定加减
            if mapping[prev_char] > mapping[current_char]:
                total_value -= current_value
            else:
                total_value += current_value
            prev_char = current_char
        return total_value
                
            

class Solution1:
    """
    思路：直接利用 List 的 reverse 思路，比较当前字符和上一个字符的数值大小。
    优点：利用 Stack 思路是一致的，但是节约了时间消耗
    """
    def romanToInt(self, string):
        prev_char = string[-1]
        total_value = mapping[prev_char]

        string = string[:-1]
        
        while string:
            current_char = string[-1]
            current_value = mapping[current_char]
            string = string[:-1]

            # 判断字符大小确定加减
            if mapping[prev_char] > current_value:
                total_value -= current_value
            else:
                total_value += current_value
            prev_char = current_char
        return total_value        



            

if __name__ == "__main__":
    text = "MCMXCIV" #"IX" "LVIII" #
    t = Solution1()
    print(t.romanToInt(text))