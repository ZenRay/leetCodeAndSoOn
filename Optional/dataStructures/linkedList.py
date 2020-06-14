#coding:utf8

from __future__ import absolute_import
import numbers
import copy
from collections.abc import Sequence

class Node:
    def __init__(self, value=None):
        self.value = value
        self._next = None

    def add(self, other):
        """Add Other Node"""
        # if other object is not Node, raise TypeError
        if isinstance(other, Node):
            self._next = other
        else:
            raise TypeError(f"Add Node object, but get {type(other)}")

    
    def __lt__(self, other):
        return self.value < other.value


    def __str__(self):
        """Display Address And Value"""
        return "<Node at %s Value: %s>" % (hex(id(self)), self.value)


    def __repr__(self):
        if isinstance(self.value, str):
            return "Node(value='%s')" % self.value
        elif isinstance(self.value, numbers.Number):
            return "Node(value=%s)" % self.value



class DoubleNode:
    def __init__(self, value=None):
        self.value = value
        self._next = None
        self._prev = None

    def add(self, other):
        """Add Other DoubleNode"""
        # if other object is not DoubleNode, raise TypeError
        if isinstance(other, DoubleNode):
            self._next = other
            self._next._prev = self
        else:
            raise TypeError(f"Add DoubleNode object, but get {type(other)}")

    
    def __lt__(self, other):
        return self.value < other.value


    def __str__(self):
        """Display Address And Value"""
        return "<DoubleNode at %s Value: %s>" % (hex(id(self)), self.value)


    def __repr__(self):
        if isinstance(self.value, str):
            return "DoubleNode(value='%s')" % self.value
        elif isinstance(self.value, numbers.Number):
            return "DoubleNode(value=%s)" % self.value



class SingleLinkedList:
    """
    Single lingked list object
    """
    def __init__(self, *args, values=None):
        self.head = None

        if values is None:
            values = args
        # values maybe a primitive value or a sequence value
        elif isinstance(values, Sequence):
            values = list(values) + list(args)
        else:
            values = [values]

        # update list
        for value in values:
            self.append(value)


    def append(self, value):
        """Add Node

        If head is None, it's empty linkedList. Add a Node to head. If head is 
        not None, loop the linked list and add a node.

        Exceptions:
            If value type is not string, number, raise TypeError
        """
        if isinstance(value, (numbers.Number, str)):
            newNode = Node(value=value)
        elif isinstance(value, SingleLinkedList):
            newNode = value
        else:
            raise TypeError(f"Support numeric value, string or SingleLinkedList, \
                but get {type(value)}")

        if self.head is None:
            self.head = newNode
            return None
        
        # loop list
        node = self.head
        while node._next:
            node = node._next

        # append element
        node._next = newNode
        
        return None


    def prepend(self, value):
        """Append Node At Head

        If head is None, it's empty linkedList. Add a Node to head. If head is 
        not None, add linked list to new Node.

        Exceptions:
            If value type is not string, number, raise TypeError
        """
        if not isinstance(value, (numbers.Number, str)):
            raise TypeError(f"Support numeric value or string, but get {type(value)}")

        if self.head is None:
            self.head = Node(value=value)
            return None
        
        node = Node(value=value)
        node._next = self.head
        self.head = node


    def search(self, value):
        """Search Value In Linked List"""
        if self.head is None:
            raise TypeError("Empty single linked list")

        node = self.head
        result = node.value == value
        while node._next and not result:
            result = node.value == value
            node = node._next
        
        return result
            

    def remove(self, value):
        """Remove Value In Linked List"""
        if self.head is None:
            raise TypeError("Empty single linked list")
        
        currentNode = self.head
        while True:
            if currentNode.value == value:
                self.head = currentNode._next
                return None
            # 如果没有下一个节点报错
            if not currentNode._next:
                raise ValueError(f"Value {value} not in linked list")
            else:
                currentNode = currentNode._next
        

    
    def pop(self):
        """Remove Last Node"""
        if self.head is None:
            raise TypeError("Empty single linked list")

        currentNode = self.head
        while currentNode._next._next:
            currentNode = currentNode._next
        
        result = currentNode._next.value
        # delete node
        currentNode._next = None
        return result


    def insert(self, index, value):
        """Insert Value Before Index
        
        Args:
            index: inserted value before index
            value: node value
        
        Results:
            Return None
        """
        if index == 0:
            self.prepend(value)
            return None

        startIndex = 0
        currentNode = self.head
        while currentNode:
            if startIndex >= index:
                offsetNode = currentNode._next
                currentNode._next = Node(value=value)
                currentNode._next._next = offsetNode
                return None
            elif startIndex < index:
                startIndex += 1
            else:
                raise IndexError("Single linked list index out of range")



    def size(self):
        """Linked List Length"""
        currentIndex = 0
        
        # loop until the node next value is None
        node = self.head
        while node._next:
            node = node._next
            currentIndex += 1
        
        return currentIndex + 1

    
    def __iter__(self):
        """Iterator"""
        currentNode = self.head
        while currentNode:
            yield currentNode

            # get next node
            if hasattr(currentNode, "_next"):
                currentNode = currentNode._next
            else:
                currentNode = None


    # def __str__(self):
    #     """Display Address"""
    #     return "<Single Linked List at %s>" % hex(id(self))


    def __repr__(self):
        """Display Address"""
        return "<Single Linked List at %s>" % hex(id(self))

    
    def reverse(self):
        """Reversed Single Linked List: Create a New Single Linked List"""
        values = [node.value for node in self]
        result = SingleLinkedList(values=values[::-1])
            
        return result


            
class DoubleLinkedList:
    """
    双向链表明确自己的尾部，所以可以快速的添加元素
    """
    def __init__(self, *args, values=None):
        self.head = None
        self.tail = None

        if values is None:
            values = args
        # values maybe a primitive value or a sequence value
        elif isinstance(values, Sequence):
            values = list(values) + list(args)
        else:
            values = [values]

        # update list
        for value in values:
            self.append(value)

    
    def append(self, value):
        """Add DoubleNode

        If head is None, it's empty DoubleLinkedList. Add a DoubleNode to head. 
        If head is not None, add node to tail.

        Exceptions:
            If value type is not string, number, raise TypeError
        """
        if not isinstance(value, (numbers.Number, str)):
            raise TypeError(f"Support numeric value or string, but get {type(value)}")

        if self.head is None:
            self.head = DoubleNode(value=value)
            self.tail = self.head
            return None
        
        self.tail._next = DoubleNode(value=value)
        self.tail._next._prev = self.tail
        
        return None
    

