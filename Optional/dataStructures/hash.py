#coding:utf8
"""
哈希：

解决哈希冲突的方法：
1. 更改哈希函数中处理值
2. 调整存储数据的结构——哈希桶的思路
"""

class HashMap:
    def __init__(self, size=10):
        self.bucket = [None] * size
        self.prime = 37
        self.size = 0

    
    def put(self, key, value):
        """
        解决哈希冲突：
        通过 LinkedList 存储键值，并且以链形式串联数据
        """
        index = self.getBucketIndex(key)
        node = LinkedListNode(key, value)

        # 获取对应的桶，并更新数据——首先需要确保 key 是唯一的，所以如果key 已经存在，那么是
        # 直接更新对应的值即可
        head = self.bucket[index]

        while head is not None:
            if head.key == key:
                head.value = value
                return
            # 更新下一个 node
            head = head.next

        # 解决哈希冲突，表明插入的是一个新数据——插入的方式，是直接插在头部
        head = self.bucket[index]
        node.next = head
        self.bucket[index] = node

        # 更新 size 大小
        self.size += 1


    def get(self, key):
        """
        查询数据值
        """
        index = self.getBucketIndex(key)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None


    def delete(self, key):
        index = self.getBucketIndex(key)
        head = self.bucket[index]

        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket[index] = head.next
                else:
                    previous.next = head.next
                self.size -= 1
                return
            else:
                previous = head
                head = head.next

    def getBucketIndex(self, key):
        """
        获取哈希桶所在索引
        """
        return self.getHashCode(key)


    def getHashCode(self, key):
        hashCode = 0
        for index, char in enumerate(str(key)):
            hashCode += ord(char) * self.prime ** index

        return hashCode % len(self.bucket)


    def __repr__(self):
        output = "\nLet's view the hash map:"

        node = self.bucket
        for bucket_index, node in enumerate(self.bucket):
            if node is None:
                output += '\n[{}] '.format(bucket_index)
            else:
                output += '\n[{}]'.format(bucket_index)
                while node is not None:
                    output += ' ({} , {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next
                    
        return output




class LinkedListNode:
    """
    创建存储数据需要的 Node
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



if __name__ == "__main__":
    hmap = HashMap()
    print(hmap.getBucketIndex("abcd"))


    if True:
        # Test the collision resolution technique
        hash_map = HashMap()

        hash_map.put("one", 1)
        hash_map.put("two", 2)
        hash_map.put("three", 3)          # Collision: The key "three" will generate the same bucket_index as that of the key "two"
        hash_map.put("neo", 11)           # Collision: The key "neo" will generate the same bucket_index as that of the key "one"

        print("size: {}".format(hash_map.size))

        print("one: {}".format(hash_map.get("one")))
        print("neo: {}".format(hash_map.get("neo")))
        print("three: {}".format(hash_map.get("three")))

        hash_map                          # call to the helper function to see the hashmap

        print("Test delete")
        hash_map.delete("one")
        hash_map                          # call to the helper function to see the hashmap

        print(hash_map.get("one"))
        print(hash_map.size)