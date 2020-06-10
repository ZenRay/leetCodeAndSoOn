#coding:utf8
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from __future__ import absolute_import


class Solution1:
    """
    第一种方式，是直接通过除以 10 的方式，得到整数和余数进行逆转一次即可
    """
    def reverse(self, x: int) -> int:
        # 判断数据正负号，在结果中保留符号
        if x < 0:
            x = abs(x)
            sign = -1
        else:
            sign = 1
        
        # 第一次计算
        division = x % 10
        x = x // 10

        if division == 0:
            result = 0
        else:
            result = division

        # 得到最大和最小极限范围
        maxLimitation = pow(2, 31) - 1
        minLimitation = -pow(2, 31)
        while True:
            if x == 0:
                break

            division = x % 10
            x = x // 10
            result = result * 10 + division

            # 如果超出范围跳出为 0
            if result > maxLimitation or (result < -pow(2, 31) and sign == -1):
                return 0
        result = result * sign

        return result


class Solution2:
    """
    第二种方式是以字符串逆转求解的方式得到结果
    """

    def reverse(self, x: int) -> int:
        max_ = 0x7fffffff
        min_ = -0x80000000
        if x < 0:
            x = abs(x)
            sign = -1
        else:
            sign = 1

        x = str(x)[::-1]
        result = int("".join(x)) * sign

        if result >= max_ or result <= min_:
            return 0
        return result