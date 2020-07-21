#coding:utf8
"""
16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

https://leetcode-cn.com/problems/3sum-closest/
"""

class Solution:
    """
    思路：
    同样利用练习 15 的三数和，指针移动的方式来求解每个可能的和。差异在于需要比较目标结果差异值，
    以更新数据
    """
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        
        result = ((), 1e4)
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            # 三数和双指针移动的思路
            while left < right:
                total = nums[index] + nums[left] + nums[right]
                
                diff = target - total 
                # 每轮更新值，判断条件是差异值是否有收敛
                if abs(diff) < result[1]:
                    result = ((nums[index], nums[left], nums[right]), abs(diff))
                
                if diff == 0:
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif diff < 0:
                    right -= 1
                else:
                    left += 1
            

        return result[0]


if __name__ == "__main__":
    nums = [1,1,-1,-1,3] # [0,2,1,-3] #[-1,2,1,-4]
    target = -1
    s = Solution()
    print(s.threeSumClosest(nums, target))