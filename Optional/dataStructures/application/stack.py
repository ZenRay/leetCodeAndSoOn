#coding:utf8
"""
使用 List 表达 Stack
"""


class Stack:
    def __init__(self, array_size=10):
        self.array = [None] * array_size
        self._array_size = array_size
        self.next = 0
        self.size = 0


    def _handle_full_stack(self):
        """
        处理 Stack 容量大小即将满的情况，为了保证元素的连续行，采取将按原有大小增大两倍并将
        元素复制到新的 list 中
        """
        origin = self.array.copy()
        self.array = [None] * (2 * len(origin))

        for index, element in enumerate(origin):
            self.array[index] = element
        
    
    def push(self, value):
        if self.size + 1 >= len(self.array):
            self._handle_full_stack()

        self.array[self.next] = value
        self.next += 1
        self.size += 1


    def pop(self):
        if self.is_empty:
            raise ValueError("Empty stack")
        value = self.array[self.next - 1]
        self.array[self.next - 1] = None

        return value

    @property
    def is_empty(self):
        return self.size == 0

    
    @is_empty.setter
    def is_empty(self, value):
        return NotImplemented