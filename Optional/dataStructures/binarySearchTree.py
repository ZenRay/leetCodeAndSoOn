#coding:utf8
"""
二叉树:BinarySearchTree:
有分为平衡二叉树和非平衡二叉树

二叉树的搜索、插入和删除节点的 Traverse 策略分为两种类型，一种是广度优先 BFS 一种是深度优先 DFS。
其中深度优先的策略：
1. 前序遍历, 从根结点开始（会返回作为父节点的根结点），在遍历所有完左节点之后在遍历有节点
            A
        B       C
    D
    以上二叉树以前序方式遍历的结果是 A B D C
2. 中序遍历
3. 后续遍历
"""

from __future__ import absolute_import
from functools import partial
from queue import Queue

class Node:
    def __init__(self, value=None):
        """二叉树节点需要定义左右节点"""
        self.parent = value
        self.left = None
        self.right = None

    
    @property
    def value(self):
        return self.parent


    @value.setter
    def value(self, val):
        self.parent = val


    def _hasChild(self, side=None):
        if side in ("right", "left"):
            return getattr(self, side) is not None
        else:
            raise ValueError(f"Child side isn't chosen, get {side}")


    @property
    def hasLeftChild(self):
        """Check Left Child"""
        return self._hasChild("left")

    
    @property
    def hasRightChild(self):
        """Check Right Child"""
        return self._hasChild("right")


    def _addChild(self, side, value):
        if side not in ("right", "left"):
           raise ValueError(f"Child side is right or left, get {side}") 

        if isinstance(value, Node):
            setattr(self, side, value)
        else:
            raise TypeError(f"Child should be <Node> object, get {type(value)}")

    @property
    def leftChild(self):
        return self.left

    
    @property
    def rightChild(self):
        return self.right

    
    @leftChild.setter
    def leftChild(self, val):
        self._addChild(side="left", value=val)

    
    @rightChild.setter
    def rightChild(self, val):
        self._addChild(side="right", value=val)


    def  __repr__(self):
        return f"<{self.__class__.__name__} at <{hex(id(self))}>"

    
    # def __str__(self):
    #     return f"{self.__class__.__name__} value: {self.value}\n" + \
    #         f"Has Left Child: {self.hasLeftChild}\t Has Right CHild: {self.hasRightChild}"
    
    
    def __str__(self):
        return f"Node({self.value})"
    


"""
上面 Node 是创建了节点，下面需要创建 Tree
"""
class Tree:
    def __init__(self, value):
        self.root  = Node(value)
    
    
    def getRoot(self):
        """
        获取根结点
        """
        return self.root


    @staticmethod
    def traverseWithPreOrder(tree, debug=False):
        """
        前序遍历 Tree，有几个要点需要注意：
        1. 利用 Stack 后进先出的特点，可以将遍历过的 Node 存储其中，如果子节点访问结束那么
            弹出节点——这样依赖于 Stack 的后进先出的特点就可以得到数据
        2. 需要注意访问节点的状态更新，如果没有控制父节点已经访问过左右节点的状态，那么可能导致
            子节点访问结束后没法返回到父节点，导致死循环。参考以下链接：
            * https://youtu.be/oeEhpPGYRw8
            * https://youtu.be/P1XDtgILODk
        """
        node = tree.getRoot() # 获取根结点

        visit_order = []
        visit_order.append(node.value)
        # stack 存储有访问状态的节点
        stack = Stack()
        state = State(node)
        stack.push(state)

        count = 0
        while node :
            if debug:
                print(
f"""
Loop Count: {count}
Current Node: {node.value}
Stack:
{stack}
"""
                )
            count += 1

            if node.leftChild and not state.leftVisited:
                state.leftVisited = True
                node = node.leftChild
                visit_order.append(node.value)

                # 将子节点 push 到 Stack
                state = State(node)
                stack.push(state)
            elif node.rightChild and not state.rightVisited:
                print("在右侧")
                state.rightVisited = True
                node = node.rightChild
                visit_order.append(node.value)

                # 将子节点 push 到 Stack 
                state = State(node)
                stack.push(state)
            else:
                # 如果已经访问过了左右子节点了，那么需要抛出当前 Stack 存储的节点
                stack.pop()

                # 需要根据 Stack 是否还有存储节点，如果没有节点就需要终止循环
                if not stack.isEmpty():
                    state = stack.top() # 只是获取最上层 node，但不是抛出
                    node = state.node
                else:
                    node = None
        if debug:
            print(
                f"""
Loop Count:{count}
Current Node:{node}
Stack:
{stack}
                """
            )
        return visit_order





class Stack:
    """
    Use List to imitate stack hehavior: LIFO.
    """
    def __init__(self):
        self.result = []

    
    def push(self, value):
        self.result.append(value)

    
    def pop(self):
        self.result.pop()

    
    def top(self):
        """Extract Last Element"""
        if len(self.result) > 0:
            return self.result[-1]
        else:
            return None

        
    def isEmpty(self):
        """Check Empty"""
        return len(self.result) == 0


    def __repr__(self):
        if len(self.result) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.result[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"


class State:
    """
    存储 Node 以及跟踪 Node 是否访问了左右子节点
    """
    def __init__(self, node):
        self.node = node
        self.leftVisited = False
        self.rightVisited = False

    def getNode(self):
        """返回节点"""
        return self.node

    
    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.leftVisited}
visited_right: {self.rightVisited}
        """
        return s



if __name__ == "__main__":
    if False:
        node0 = Node()
        print(f"""
        value: {node0.value}
        left: {node0.left}
        right: {node0.right}
        """)

        node0 = Node("apple")
        print(f"""
        value: {node0.value}
        left: {node0.left}
        right: {node0.right}
        """)

        node0 = Node("apple")
        node1 = Node("banana")
        node2 = Node("orange")
        node0.leftChild = node1
        node0.rightChild = node2

        print(f"""
        node 0: {node0.value}
        node 0 left child: {node0.left.value}
        node 0 right child: {node0.right.value}
        """)

        # check if left or right child exists
        node0 = Node("apple")
        node1 = Node("banana")
        node2 = Node("orange")

        print(f"has left child? {node0.hasLeftChild}")
        print(f"has right child? {node0.hasRightChild}")

        print("adding left and right children")
        node0.leftChild = node1
        node0.rightChild = node2

        print(f"has left child? {node0.hasLeftChild}")
        print(f"has right child? {node0.hasRightChild}")

    # 测试树搜索
    if True:
        tree = Tree("aple")
        tree.getRoot().leftChild = Node("ban")
        tree.getRoot().rightChild = Node("cheer")
        tree.getRoot().leftChild.leftChild = Node("dates")

        print(Tree.traverseWithPreOrder(tree, True))