#coding:utf8
"""
11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
![](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg)
图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。 

示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from itertools import combinations

class Solution:
    """
    暴力求解，直接将数据进行组合计算出最大值组合,缺点是时间消耗巨大
    """
    def maxArea(self, height: list) -> int:
        # 创建序列组合
        indexes = list(combinations(range(len(height)), 2))
        # 获取最大值索引
        areas = []
        for prev, lag in indexes:
            areas.append(min(height[prev], height[lag]) * (lag - prev))

        return max(areas)



class Solution1:
    """
    求解方式是两端向中间靠拢，两侧移动的条件是移动最小的柱子——在宽度在恒定变小的情况下，那么尽量
    期望下一个柱子是最大的
    """
    def maxArea(self, height: list)->int:
        area = 0
        start = 0
        end = len(height) - 1

        while start < end:
            current_area = min(height[start], height[end]) * (end - start)
            area = max(area, current_area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return area


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7] * 90
    s = Solution1()
    print(s.maxArea(height))