from queue import Queue


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def clear(self):
        del self.items[:]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.parent = None
        self.right = None
        self.left = None

    def getKey(self):
        return self.key
    # may not be used

    def getItem(self):
        return self.item

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def getParent(self):
        return self.parent

    def hasRightChild(self):
        return True if self.right else False

    def hasLeftChild(self):
        return True if self.left else False

    def isRoot(self):
        return True if self.parent else False

    def isLeaf(self):
        return True if (not self.right) and (not self.left) else False

    def isRightChild(self):
        return True if(self.parent.right == self) else False

    def isLeftChild(self):
        return True if(self.parent.left == self) else False

    def setParent(self, p):
        self.parent = p

    def setKey(self, key):
        self.key = key
        # may not be used

    def setItem(self, item):
        self.item = item

    def addRightChild(self, n):
        a = Node(n, 0)
        self.right = a

    def addLeftChild(self, n):
        a = Node(n, 0)
        self.left = a
        # Binary Tree class


class BinaryTree:
    def __init__(self):
        self.root = None
        self.pos = None
        self.size = 0

    def isEmpty(self):
        return True if not self.size else False

    def getSize(self):
        return self.size

    def getRoot(self):
        return self.root

    def getPosition(self):
        return self.pos

    def setRoot(self, node):
        self.root = node

    def setPosition(self, node):
        self.pos = node
        # locate the node with the key, where the "node" parameter is the staring node for locating process

    def findPosition(self, node, key):
        if(node):
            if(node.key == key):
                return node
            a = self.findPosition(node.left, key)
            if(not a):
                a = Node('0', 0)
            b = self.findPosition(node.right, key)
            if(not b):
                b = Node('0', 0)
            return a if a.key == key else b
        #
        # For management, print the binary tree in pre-order
        #

    def printBinaryTreeinPreOrder(self, node):
        if(node):
            print(node.key, end='') if node.key != '-' else print('', end='')
            self.printBinaryTreeinPreOrder(node.left)
            self.printBinaryTreeinPreOrder(node.right)


def readLines():
    with open('inFileA.txt', "r+") as f:
        entryListA = [x.strip() for x in f.readlines()]
    f.close()
    with open('inFileB.txt', "r+") as f:
        entryListB = [x.strip() for x in f.readlines()]
    f.close()

    return entryListA, entryListB


def constructingBinaryTree(entryList):
    #
    # read the input information from the default input text file into an
    # entry list, entryList
    #
    # initiating a binary tree b and return it after the consruction
    #
    b = BinaryTree()
    line = entryList[0].split()
    b.root = Node(line[0], 0)
    b.root.addLeftChild(line[1])
    b.root.addRightChild(line[2])
    for i in range(1, len(entryList)):
        line = entryList[i].split()
        now = b.findPosition(b.root, line[0])
        now.addLeftChild(line[1])
        now.addRightChild(line[2])
    return b

# Python program to check if two given trees are isomorphic

# A Binary tree node


def deriveTheDistance2(bt1Node, bt2Node):  # 沒做好
    q1 = Stack()
    q2 = Stack()
    s = Stack()
    q1.push(bt1Node)
    q2.push(bt2Node)
    s.push(0)
    now1 = bt1Node
    now2 = bt2Node
    sw = 0
    a = 0
    while(q1 and q2):
        if(now1.isLeaf() and now2.isLeaf()):
            now1 = q1.pop()
            now2 = q2.pop()
            sw = s.pop()
            if(sw == 1):
                now1 = now1.right
                now2 = now2.left
            else:
                now1 = now1.right
                now2 = now2.right
        elif(now1.left.key == now2.left.key):
            s.push(0)
            q1.push(now1)
            q2.push(now2)
            now1 = now1.left
            now2 = now2.left
        elif(now1.left.key == now2.right.key):
            s.push(1)
            q1.push(now1)
            q2.push(now2)
            a += 1
            now1 = now1.left
            now2 = now2.right
    return a


def swapChild(node1):
    temp = node1.left
    node1.left = node1.right
    node1.right = temp


def compare(bt1Node, bt2Node):
    if(bt1Node.left and bt1Node.right and bt2Node.left and bt2Node.right):
        if(bt1Node.left.key == bt2Node.right.key):
            return 1
        else:
            return 0
    elif(not bt2Node.left and bt2Node.right):
        if(bt1Node.right == None and bt1Node.left.key == bt2Node.right.key):
            return 1
        else:
            return 0
    else:
        if(bt1Node.left == None and bt1Node.right.key == bt2Node.left.key):
            return 1
        else:
            return 0


def deriveTheDistance(bt1Node, bt2Node):
    count = 0
    if(bt1Node.hasLeftChild() or bt1Node.hasRightChild()):
        if(compare(bt1Node, bt2Node)):
            swapChild(bt2Node)
            count += 1
        count += deriveTheDistance(bt1Node.left, bt2Node.left)
        count += deriveTheDistance(bt1Node.right, bt2Node.right)
    return count


entryList1, entryList2 = readLines()
bt1 = constructingBinaryTree(entryList1)
bt2 = constructingBinaryTree(entryList2)
print("preorder of tree 1: ", end='')
bt1.printBinaryTreeinPreOrder(bt1.getRoot())
print()
print("preorder of tree 2: ", end='')
bt2.printBinaryTreeinPreOrder(bt2.getRoot())
# a = isIsomorphic(bt1.root, bt2.root)
print()
# print(deriveTheDistance2(bt1.root, bt2.root))
print("The distance between two isomorphic binary trees is",
      deriveTheDistance(bt1.root, bt2.root))
