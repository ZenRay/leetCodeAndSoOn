#coding:utf8
"""
归并排序：
归并排序的方式，本质上是一个分治法，首先将结果拆分到最小的二元值比较大小，之后将每个二元值逐渐
合并到一起使其变长
"""

class MergeSort:
    def conquer(self, left, right):
        """合并步骤
        将得到结果的左右结果进行比较排序
        """
        result = []

        # 记录每个步骤的索引，直接通过比较大小保留留下的索引，这样就达到了更新数据值的结果
        rindex, lindex = 0, 0
        while lindex < len(left) and rindex < len(right):
            if left[lindex] < right[rindex]:
                result.append(left[lindex])
                lindex += 1
            else:
                result.append(right[rindex])
                rindex += 1
            
        # 把余下的结果添加到结果中，这里有一个细节即每个分组的 left 和 right 之间的长度差异
        # 不会大于一个——因为在分治中拆分的过程会确保是从中间拆分，那么即使在奇数个数元素的
        # 情况也最多差异一个
        result += right[rindex:]
        result += left[lindex:]

        return result

    
    def divied(self, array):
        """
        分治法中的拆分
        """
        if len(array) <= 1:
            return array

        # 平均拆分
        middle = len(array) // 2

        # 回归调用自身，以实现拆分
        left = self.divied(array[:middle]) # left
        right = self.divied(array[middle:]) # right

        return self.conquer(left, right)


if __name__ == "__main__":
    t = MergeSort()
    print(t.conquer([1,3,7], [2,5,6]))
    print(t.divied([1,23, 7, 0, 23, 2,5,6]))