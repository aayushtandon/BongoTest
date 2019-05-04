class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def findPath(root, path, k):
    if root is None:
        return False

    path.append(root.key)
    if root.key == k:
        return True

    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right != None and findPath(root.right, path, k))):
        return True
    path.pop()
    return False

def LCA(root, node1, node2):
    import psutil
    import time
    import os
    start = time.time()
    path1 = []
    path2 = []
    if (not findPath(root, path1, node1) or not findPath(root, path2, node2)):
        return -1
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    end = time.time()
    process = psutil.Process(os.getpid())
    print 'Memory requirements in bytes is:- '+str(process.memory_info().rss)
    print 'runtime in seconds is:- '+str(end-start)
    return path1[i - 1]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)

print 'The LCA is:- '+str(LCA(root, 6, 7))
print ('###########')
print 'The LCA is:- '+str(LCA(root, 3, 7))
print ('###########')
