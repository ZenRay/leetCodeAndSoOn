#coding:utf8

def bubble_sort(array):
    """
    冒泡排序：直接一个个比较大小，将最大的数据值放到最后
    """
    # 保留一个结果副本，以保留裁剪过程不影响原始数据大小
    result = array.copy() 
    while array:
        for index in range(1, len(array)):
            if result[index] < result[index - 1]:
                result[index], result[index - 1] = result[index - 1], result[index]

        # 利用现有 array 的长度裁剪一个，以控制长度得到结果
        array = result[:len(array) - 1]

    return result


def bubble_sort_version2(array):
    """
    冒泡排序: 利用两层循环的思路去解决排序问题，外层循环控制循环次数——利用的原理是冒泡排序需要的
    迭代次数是 n - 1 次
    """
    # 外层设置迭代次数
    for iteration in range(len(array) - 1):
        for index in range(1, len(array)):
            this = array[index]
            prev = array[index - 1]

            if prev > this:
                array[index] = prev
                array[index - 1] = this 
    return array

if __name__ == "__main__":
    wakeup_times = [4, 3, 2, 1]#[16,49,3,12,56,49,55,100,120, 490,46,19,55,46,13,25,56,9,48,45] #[3, 1, 2]
    print(bubble_sort_version2(wakeup_times))