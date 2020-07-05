#coding:utf8
"""
使用 List 表达 Stack
"""
import copy

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


"""
第二个版本：
第二个版本处理的方式，不是使用 List 来模拟，而是直接使用节点的方式。所以在处理上需要分别使用
Node 和对应的数据来处理
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack2:
    def __init__(self):
        self.head = None
        self.size = 0

    
    def push(self, value):
        self.size += 1
        if self.head is None:
            self.head = Node(value)
        else:
            # 直接将新 Node 放在最前面，这样就是不用遍历数据，达到了 Stack 插入数据更快的效果
            node = Node(value)
            node.next = self.head
            self.head = node
        

    def is_empty(self):
        return self.size == 0

    
    def pop(self):
        if self.is_empty():
            return None
            
        value = self.head.value
        self.size -= 1
        self.head = self.head.next
        return value

    
    def top(self):
        return self.head.value

    
    @staticmethod
    def reverse(stack):
        stack = copy.deepcopy(stack)
        result = Stack2()
        while True:
            value = stack.pop()
            if value is None:
                return result
            else:
                result.push(value)