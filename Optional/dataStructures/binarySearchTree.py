#coding:utf8
"""
二叉树:BinarySearchTree:
有分为平衡二叉树和非平衡二叉树
"""

from __future__ import absolute_import
from functools import partial

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

    
    def __str__(self):
        return f"{self.__class__.__name__} value: {self.value}\n" + \
            f"Has Left Child: {self.hasLeftChild}\t Has Right CHild: {self.hasRightChild}"

