#coding:utf8
"""
队列：LILO
在方法实现上，以入队(enqueue)和出队(dequeue)的方式进行管理元素
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        """
        队列中，创建 head 和 tail 属性可以分别用于用于控制队列中 head 和 tail，这样在处理
        入队的时候可以快速插入，避免使用循环的方式查询之后在入队。优点是降低了时间消耗
        """
        self.head = None
        self.tail = None
        self.size = 0


    def enqueue(self, value):
        """
        入队的方法，需要将数据插入到最后一个
        """
        
        if self.size == 0:
            self.head = Node(value) 
            self.tail = self.head
        else:
            node = self.head.next
            self.tail.next = Node(value)
            self.tail = self.tail.next

        # 更新 size 大小
        self.size += 1

    
    def dequeue(self):
        """
        出对方法，需要将第一个数据弹出，因此需要更新的是 head 的节点由后续的 Node 接上
        """
        if self.size == 0:
            raise StopIteration("Empty Queue")

        value = self.head.value
        node = self.head.next
        self.head = node
        self.size -= 1
        return value

    
    def front(self):
        """
        返回队列第一个值，但不删除
        """
        if self.size == 0:
            raise StopIteration("Empty Queue")

        return self.head.value

    
    def is_empty(self):
        """
        队列是否为空
        """
        return self.size == 0


"""
第二种方式处理 Queue，思路是利用 Stack 进行处理:
1. 需要分别建立两个 Stack，一个用于快速处理入队，一个处理出对
2. 出入队列的处理，入队优先将数据写入入队 Stack，出对队列需要判断出对 Stack 是否存在，
    如果存在可以直接返回结果；如果不存在需要逆向先将入队 Stack pop 出数据写入出对 Stack，这样
    就达到了逆向排序的目的
"""
class Stack:
    def __init__(self):
        self.items = []
    
    @property
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size == 0:
            return None
        else:
            return self.items.pop()

class Queue2:
    def __init__(self):
        self.instorage = Stack()
        self.outstorage = Stack()
    
    @property
    def size(self):
        return self.outstorage.size + self.instorage.size


    def enqueue(self, value):
        self.instorage.push(value)


    def dequeue(self):
        """
        """
        if not self.outstorage.items:
            while self.instorage.items:
                self.outstorage.push(self.instorage.pop())
        return self.outstorage.pop()


if __name__ == "__main__":
    q = Queue2()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test size
    print ("Pass" if (q.size == 3) else "Fail")

    # Test dequeue
    print ("Pass" if (q.dequeue() == 1) else "Fail")

    # Test enqueue
    q.enqueue(4)
    print ("Pass" if (q.dequeue() == 2) else "Fail")
    print ("Pass" if (q.dequeue() == 3) else "Fail")
    print ("Pass" if (q.dequeue() == 4) else "Fail")
    q.enqueue(5)
    print ("Pass" if (q.size == 1) else "Fail")