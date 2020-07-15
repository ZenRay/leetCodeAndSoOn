#coding:utf8
"""
二叉搜索树
"""
class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"


from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


class Tree():
    def __init__(self):
        self.root = None
        
    def set_root(self,value):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1
    
    """
    define insert here
    can use a for loop (try one or both ways)
    """
    def insert_with_loop(self,new_value):
        """
        插入数据，如果重复的话，则覆盖
        TODO: 可以以其他方式处理重复数据
        """
        new_node = Node(new_value)

        if self.root is None:
            self.root = new_node
            return

        node = self.root
        while True:
            comparision = self.compare(node, new_node)
            # 数据和当前节点值相同
            if comparision == 0:
                node.set_value(new_node.get_value())
                break
            # 数据值比当前节点小
            elif comparision == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break
            # 当前数据比当前节点值大
            elif comparision == 1:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break

            


    """
    define insert here (can use recursion)
    try one or both ways
    """  
    def insert_with_recursion(self,value):
        def recursion(node, value):
            new_node = Node(value)
            comparision = self.compare(node, new_node)

            if comparision == 0:
                return 
            elif comparision == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                    recursion(node, value)
                else:
                    node.set_left_child(new_node)
                    return 
            elif comparision == 1:
                if node.has_right_child():
                    node = node.get_right_child()
                    recursion(node, value)
                else:
                    node.set_right_child(new_node)
                    return


        if self.root is None:
            self.root = Node(value)
            return 
        node = self.root
        recursion(node, value)


    def search(self,value):
        """
        implement search
        """
        if self.root is None:
            return False
        
        node = self.root
    
        while node:
            comparision = self.compare(node, Node(value))
            if comparision == 0:
                return True
            # 小于当前节点值
            elif comparision == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False
            # 大于当前节点值
            elif comparision == 1:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False

    def delete(self, value):
        """
        删除子树，需要分为三种情况：
        1. 没有子节点的情况，属于也节点
        2. 有一个子节点的情况
        3. 有两个子节点情况
        """
        def recursion(node, value):
            comparision = self.compare(node, Node(value))
            if comparision == 0:
                if node.has_left_child() and node.has_right_child():
                    # TODO: 需要完成更新左右子节点都存在的情况
                    pass
                elif node.has_left_child() and not node.has_right_child():
                    parent_node = queue.deq()
                    parent_node.set_right_child(None)
                    parent_node.set_left_child(None)
                else:
                    parent_node = queue.deq()
                    if node.has_left_child():
                        parent_node.set_left_child(node.get_left_child())
                        return
                    else:
                        parent_node.set_right_child(node.get_right_child())
                        return
                return
            elif comparision == -1:
                if node.has_left_child():
                    queue.enq(node)
                    node = node.get_left_child()
                    queue.deq()
                    return recursion(node, value)
            elif comparision == 1:
                if node.has_right_child():
                    queue.enq(node)
                    node = node.get_right_child()
                    queue.deq()
                    return recursion(node, value)
                
                    

        node = self.root
        queue = Queue()
        queue.enq(node)
        recursion(node, value)


            

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

                
        return s


if __name__ == "__main__":
    if False:
        tree = Tree()
        tree.insert_with_loop(5)
        tree.insert_with_loop(6)
        tree.insert_with_loop(4)
        tree.insert_with_loop(2)
        tree.insert_with_loop(5) # insert duplicate
        print(tree)

    if False:
        tree = Tree()
        tree.insert_with_recursion(5)
        tree.insert_with_recursion(6)
        tree.insert_with_recursion(4)
        tree.insert_with_recursion(2)
        tree.insert_with_recursion(5) # insert duplicate
        print(tree)

    if True:
        tree = Tree()
        tree.insert_with_recursion(5)
        tree.insert_with_recursion(6)
        tree.insert_with_recursion(4)
        tree.insert_with_recursion(2)


        # print(f"""
        # search for 2: {tree.search(2)}
        # search for 8: {tree.search(8)}
        # """)
        tree.delete(6)
        print(tree)
        # print(tree)