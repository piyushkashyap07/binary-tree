
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

#Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nodesnumber(root):
    if root is None:
        return 0
    leftcount=nodesnumber(root.left)
    rightcount=nodesnumber(root.right)
    return 1+leftcount+rightcount
    