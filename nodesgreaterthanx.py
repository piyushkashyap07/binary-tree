from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def countNodesGreaterThanX(root, x) :
    if root is None:
        return 0
    count=0
    if root.data>x:
        count+=1
        
    left=countNodesGreaterThanX(root.left,x)
    right=countNodesGreaterThanX(root.right,x)
    return count+left+right

	#Your code goes here
#     return helpfunction(root,x)
    
# def helpfunction(root,x,count=0):
#     if root==None:
#         return
#     if root.left is not None:
#         count = helpfunction(root.left,x, count)
#         if root.left.data > x:
#             count+=1
#         return count
    
#     if root.right is not None:
#         count = helpfunction(root.right,x, count)
#         if root.right.data > x:
#             count+=1
#         return count
    
#     if root.data>x:
#         count+=1
#         return count
    
#     return count

        
    
    
    
































		



#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

# Main
root = takeInput()
x = int(stdin.readline().strip())

count = countNodesGreaterThanX(root, x)
print(count)