#coding:utf8
"""
Trie: 是一个前缀树或称为字典树，是一种有序对树。例如下面的数据可以用于存储单词 a, add 以及 hi，
它是一个 trie 的示例：
{
    # a  和 add 两个单词
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False},
        'word_end': True},
    # hi 单词
    'h': {
        'i': {'word_end': True},
        'word_end': False}}

在实际应用中可以利用树的形式来表达树
"""

from collections import defaultdict
class Node:
    def __init__(self):
        self.wordEnd = False
        self.children = defaultdict(Node)


class Trie:
    def __init__(self):
        self.root = Node()
        self.size = 0


    def add(self, word):
        """
        添加单词
        """
        current_node = self.root

        for char in word:
            # * 如果不存在字符作为键时，需要添加 Node
            if char not in current_node.children:
                current_node.children[char] = Node()
            # * 更新需要作为子节点的字符键
            current_node = current_node.children.get(char)
        # * 结束循环表示当前单词字符循环完成
        current_node.wordEnd = True
            

    def isExist(self, word):
        current_node = self.root

        for char in word:
            # * 只要存在字符不再子节点中，那么返回 False
            if char not in current_node.children:
                return False
            current_node = current_node.children.get(char)
        return current_node.wordEnd


if __name__ == "__main__":
    words = ['they', 'an', 'there', 'answer', 'any', 'the', 'by', 'bye', 'their']
    trie = Trie()

    for valid_word in words:
        trie.add(valid_word)

    assert trie.isExist('the')
    assert trie.isExist('any')
    assert not trie.isExist('these')
    assert not trie.isExist('zzz')
    print('All tests passed!')