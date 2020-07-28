#coding:utf8
"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
![](https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/17_telephone_keypad.png)


示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    思路：
        利用循环的方式进行处理：
        1. 如果为第一个字符时保存下每个当前数字字符对应的列表
        2. 之后的数字字符，只需要将对应的字符列表和之前的结果进行遍历求解
    """
    hashWords = {
        "2": "abc",
        "3": "def", 
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    def letterCombinations(self, digits):
        if len(digits) < 1:
            return []
        elif len(digits) == 1:
            return list(self.hashWords[digits])
        
        result = []
        for digit in digits:
            if len(result) == 0:
                result = list(self.hashWords[digit])
                continue
            result = [prev + post for prev in result for post in self.hashWords[digit]]
        
        return result


    def letterCombinations2(self, digits):
        """
        调整上面的代码，思路同样是循环的思路，但通过递的方式实现回溯来解决问题
        时间复杂度： $O(3^N \times 4^M)$，N 和 M 分别对应的数字字符有三位和四位的个数，
            例如 1、2、3 等就只有三位，7、9 有四位
        """
        result = []
        def combine(combinations, next_digits):
            # * 如果下一个数字字符为空，那么直接将已经完成的结果添加到 result 中
            if len(next_digits) == 0:
                result.append(combinations)
            else:
                # * 分别将下一个数字字符对应的字符，和之前的结果进行结合作为新结果，继续调用
                # * 自身函数（递归）
                for char in self.hashWords[next_digits[0]]:
                    combine(combinations + char, next_digits[1:])
        # ! 需要在 local 函数外有一个可变的对象（result）用于存储最终结果，调用函数返回结果
        combine("", digits)
        return result



if __name__ == "__main__":
    digits = "234"
    s = Solution()
    print(s.letterCombinations2(digits))