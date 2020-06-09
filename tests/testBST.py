#coding:utf8

from __future__ import absolute_import
import os
import sys
import unittest

sys.path.append("..")

from Optional.dataStructures import binarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        """测试前置操作

        可能同时存在多个前置操作相同的测试，我们可以把测试的前置操作从测试代码中拆解出来，
        并实现测试前置方法 setUp() 
        """
        self.node = binarySearchTree.Node(23)


    def testCurrentValue(self):
        self.assertEqual(self.node.value, 23, "Incorrect Current Value")

    
    def testHasChild(self):
        self.assertEqual(self.node.hasLeftChild, False, 
                        "Initial Node has left child")
        self.assertEqual(self.node.hasRightChild, False, 
                        "Initial Node has right Child")


    def tearDown(self):
        """测试后置操作

        setUp() 出现错误，测试方法不会运行。但是无论测试方法是否成功，都会运行 tearDown()。
        这样的一个测试代码运行的环境被称为 test fixture 。一个新的 TestCase 实例作为一个
        测试脚手架，用于运行各个独立的测试方法。在运行每个测试时，setUp() 、tearDown() 和
         __init__() 会被调用一次
        """
        pass
        

if __name__ == "__main__":
    unittest.main()