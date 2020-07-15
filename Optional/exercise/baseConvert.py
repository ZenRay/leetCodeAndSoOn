#coding:utf8
"""
进制转换
"""

class BaseConversion:
    """
    数字数据的进制转换
    """
    def toDecimalDiv(self, value:str, base:int):
        """
        转换为 10 进制的整数部分，value 为整数部分值，base 为当前 value 的进制
        """
        result = 0
        for byte in value:
            result = result * base + int(byte) * base
        return result // base


    def toDecimalMod(self, value:str, base:int):
        """
        小数部分转换为 10 进制数据，value 为小数部分值，base 为当前 value 的进制
        """
        # 空字符串的情况下返回 0，即没有小数部分
        if value:
            return 0

        result = 0
        for byte in value[::-1]:
            result = (result + int(byte)) / base
        return result 

    def binary2decimal(self, string:str):
        """
        二进制转换为十进制:
        1. 整数部分，除以 10 得到整数和余数，余数乘以 2 作为结果
        2. 整数部分继续除以 10 得整数和余数，余数加上结果乘以 2 作为新的结果
        3. 循环上面步骤 2
        """
        values = string.split(".")
        
        if len(values) == 2:
            return self.toDecimalDiv(values[0], 2) + self.toDecimalMod(values[1], 2)
        elif len(values) == 1:
            return self.toDecimalDiv(values[0], 2)
        else:
            raise ValueError("输入错误，有多个小数点")


if __name__ == "__main__":
    t = BaseConversion()
    print(t.binary2decimal("1101."))