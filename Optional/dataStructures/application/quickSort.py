#coding:utf8
"""
quickSort: 快排的方式是筛选一个随机的数据作为基准(Pivot)，将其他数据和基准比较将数据放在基准两
侧。之后在从基准两侧重新选择两个基准，对两侧数据排序。

需要注意在进行数据排序处理的过程中，需要控制给移动数据腾出空间。假设 [8, 2, 4, 7, 0, 3, 1] 
数据排序，首先选择最后一个作为基准(一般是选择最前或者最后作为基准，并非完全随机)，那么在移动的方案
是需要将 1 之前一个空间空出，这样就可以根据相应的数据移动了—— 3 位置空出，1 移动到 3 的位置，
第一个比较数据值 8 就可以移动到最后了。

在时间效率上，最糟糕的情况下是 $O(N^2)$，平均时间效率上是 $O(N \times \log(N))$
"""
def single(array, begin_index, end_index):
    """单轮排序获取基准索引"""
    start_index = begin_index
    pivot_index = end_index
    pivot = array[pivot_index]

    while start_index != pivot_index:
        start = array[start_index]

        # 不需要换位置的情况
        if start <= pivot:
            start_index += 1
            continue

        # 首先将基准索引前一位数据放到检验的数据索引上
        array[start_index] = array[pivot_index - 1]

        # 将基准前移一位
        array[pivot_index - 1] = pivot

        # 将比较的数据值放在基准索引上
        array[pivot_index] = start

        # 更新基准索引
        pivot_index -= 1
    return pivot_index

def naive_quick_sort(array):
    """简单快排
    该方式是没有优化的排序方案，直接对数据进行循环的方式排序
    """
    def sort(array, begin_index, end_index):
        if end_index <= begin_index:
            return 
        # 将基准索引前后分为两部分排序
        pivot_index = single(array, begin_index, end_index)
        sort(array, begin_index, pivot_index - 1)
        sort(array, pivot_index + 1, end_index)
    
    sort(array, 0, len(array) - 1)


if __name__ == "__main__":
    array = [8, 3, 1, 7, 0, 10, 2, 100, 3, 2, 1]
    naive_quick_sort(array)
    print(array)
