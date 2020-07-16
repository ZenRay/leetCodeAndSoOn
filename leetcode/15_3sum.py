#coding:utf8
"""
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
https://leetcode-cn.com/problems/3sum/
"""
import numpy as np
from itertools import combinations


class Solution1:
    """
    利用首尾双指针的思路：
    首尾指针和的数字和当前位置数据求和比较，作为移动首尾指针的参考
    时间复杂度为 O(N logN)
    """
    def threeSum(self, nums):
        nums = sorted(nums)

        result = []
        # 固定一个位置
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            first = index + 1
            second = len(nums) - 1
            while first < second:
                if nums[index] + nums[first] + nums[second] == 0:
                    result.append([nums[index], nums[first], nums[second]])
                    # 需要解决当前位置和下一个位置数字是相同的情况
                    while first < second and nums[first] == nums[first + 1]:
                        first += 1
                    
                    while second > first and nums[second] == nums[second - 1]:
                        second -= 1

                    first += 1
                    second -= 1
                elif nums[index] + nums[first] + nums[second] < 0:
                    first += 1
                else:
                    second -= 1

        return result

    
    def twoSum(self, nums, target):
        start = 0
        end = len(nums) - 1
        result = []
        while start < end:
            if nums[start] + nums[end] == target:
                result.append([nums[start], nums[end], target])

                # 调整首尾位置，如果下个数据和当前相同的情况需要移动一个
                while nums[start] == nums[start + 1]:
                    start += 1
                
                while nums[end] == nums[end - 1]:
                    end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return result




class Solution:
    """
    直接暴力解法：
    1. 解决掉重复的问题，排序得到的数字序列可以排除掉组合重复的问题
    2. 第一个指针明确，第二个指针和第三个指针利用组合的方式得到
    3. 判断是否满足第一个指针数字等于二三指针数字和，同时结果中没有保存到的组合才保存
    缺点：时间复杂度为 O(N^3)
    """
    def threeSum(self, nums):
        nums = sorted(nums)
        result = []
        for first in range(len(nums)-2):
            rest_nums = nums[first+1:]
            for second, third in combinations(range(len(rest_nums)), 2):
                if nums[first] * -1 == rest_nums[second] + rest_nums[third]:
                    if [nums[first], rest_nums[second], rest_nums[third]] not in result:
                        result.append([nums[first], rest_nums[second], rest_nums[third]])

        
        return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4] # [1,2,-2,-1] #
    s = Solution1()
    print(s.threeSum(nums))