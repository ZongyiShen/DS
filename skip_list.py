import re
import random

# Two special values for boundary nodes
PLUS_INF = 99999
MINUS_INF = -99999

# Node class definition: a quadraic node having four links


class SLnode:
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.up = None
        self.down = None
        self.next = None
        self.prev = None

    def getKey(self):
        return self.key

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def getUp(self):
        return self.up

    def getDown(self):
        return self.down

    def hasNext(self):
        return (self.next != None)

    def hasPrev(self):
        return (self.prev != None)

    def setKey(self, key):
        self.key = key

    def setItem(self, item):
        self.item = item

    def setNext(self, p):
        self.next = p

    def setPrev(self, p):
        self.prev = p

    def setUp(self, p):
        self.up = p

    def setDown(self, p):
        self.down = p

# List class definition used in the skip list


class SLlist:
    def __init__(self):
        self.leftDummy = SLnode(MINUS_INF, "")
        self.rightDummy = SLnode(PLUS_INF, "")
        self.leftDummy.setNext(self.rightDummy)
        self.rightDummy.setPrev(self.leftDummy)
        self.size = 0
        self.insert_cursor = self.getleftDummy()

    def getleftDummy(self):
        return self.leftDummy

    def getrightDummy(self):
        return self.rightDummy

    def getSize(self):
        return self.size

    def increaseSize(self):
        self.size = self.size + 1

    def decreaseSize(self):
        self.size = self.size - 1

    def isEmpty(self):
        if(self.leftDummy.next == self.rightDummy):
            return True
        return False
    '''
    method insertAfter(self, p, SLnode): insert a node in the list after node p
    '''

    def insertAfter(self, p, SLnode):
        p.setNext(SLnode)
        p.next.setPrev(p)
        self.increaseSize()
    '''
    method print_List(self): print the content of the list
    '''

    def print_List(self):
        now = self.leftDummy
        s = ""
        while(now != self.rightDummy):
            s += "({0},{1})".format(str(now.key), now.item)
            #print((now.key, now.item), end=' ')
            now = now.next
        s += "({0},{1})".format(str(now.key), now.item)
        #print((now.key, now.item))
        print(s)
        # Skip list definition: a list of lists is used


def coin_tossing():
    i = 1
    a = random.randint(0, 1)
    while(a):
        i += 1
        a = random.randint(0, 1)
    return i


class Skip_Lists:
    def __init__(self):
        self.S = [SLlist()]

    def getLists(self):
        return self.S

    # use the number of nodes in the bottom list to denote the Size
    def getSize(self):
        return self.S[0].getSize()

    # use Height to denote the number of lists used in the skip list
    def getHeight(self):
        return len(self.S)

    def isEmpty(self):
        return ((self.getHeight() == 1) and (self.getSize() == 0))

    # Derive the top list in the skip list
    def getTopList(self):
        return self.S[self.getHeight()-1]

    '''
    method getTopleft(self): get the topleft node in the skip list
    '''
    # Derive the topleft node in the skip list

    def getTopleft(self):
        return self.S[self.getHeight()-1].leftDummy
    '''
    method addEmptyList(): padding the skip list when the number of copies of the inserted node
    is more than the height of the current  skip list
    '''

    def addEmptyList(self):
        now1 = self.getTopleft()
        self.S.append(SLlist())
        now1.up = self.getTopleft()
        self.getTopleft().down = now1

    def delEmptyList(self):
        while(self.S[self.getHeight()-2].isEmpty() and self.getHeight() > 1):
            now = self.S[self.getHeight()-2]
            now.leftDummy.up.down = now.leftDummy.down
            if(now.leftDummy.down):
                now.leftDummy.down.up = now.leftDummy.up
            self.S.remove(self.S[self.getHeight()-2])

    '''
    method search(node): search the skip list with the given node using the key
    '''

    def search(self, node):
        now = self.getTopleft()
        while(1):
            if(now.next.key < node.key):
                now = now.next
            elif(now.down):
                now = now.down
            elif(node.key == now.next.key):
                return now.next
            else:
                return 0

    '''
    method delete(node): delete the given node from the skip list
    '''

    def delete(self, node):
        now = self.search(node)
        if(not now):
            print("Key not found in the skip lists and will not perform the deletion")
            return
        while(now):
            now.prev.next = now.next
            now.next.prev = now.prev
            now = now.up
        self.delEmptyList()

    '''
    method insert(node): insert the given node to the skip list
    '''

    def insert(self, node):
        if(self.search(node)):
            print("Key found in the skip lists and will not inert the new node")
            return
        level = coin_tossing()
        # print(self.getHeight())
        if(self.getHeight() < level):
            self.addEmptyList()
            level = self.getHeight()
        now = self.S[0].leftDummy
        temp2 = 0
        while(1):
            if(level == 0):
                break
            if(not now):
                break
            if(now.next.key < node.key):
                now = now.next
            elif(node.key < now.next.key):
                temp = SLnode(node.key, node.item)
                temp.down = temp2
                if(temp2):
                    temp2.up = temp
                now.next.prev = temp
                temp.next = now.next
                now.next = temp
                temp.prev = now
                temp2 = temp
                now = now.up
                level -= 1
        if(not self.getTopList().isEmpty()):
            self.addEmptyList()
        self.delEmptyList()


'''
function for coin tossing with the number of heads returned
'''


'''
function for reading lines (entries) in the input text file into a list of strings
'''


def read_lines():
    f = open('inFile-2.txt')
    k = f.readlines()
    return k


'''
function for starting the task
'''


def create_SkipLists():
    #
    # read the input information from the default input text file into an
    # entry list, entry_list
    #
    entry_list = read_lines()
    #
    # initiating a skip list object SL
    #
    SL = Skip_Lists()
    for index in range(0, len(entry_list)):
        # splitting the string by " " symbol for deriving the entry
        pairs = re.split(" ", entry_list[index])
        # making a new node for the entry
        newnode = SLnode(int(pairs[0]), pairs[1].split('\n')[0])
        # inserting the new node to the skip list SL
        SL.insert(newnode)

    # --------------dynamic operations with result printed -----------------------------------
    for i in range(0, SL.getHeight()):
        SL.S[i].print_List()

    print("Insert (88, luke)")
    SL.insert(SLnode(88, "luke"))
    for i in range(0, SL.getHeight()):
        SL.S[i].print_List()

    print("delete (40, kite)")
    SL.delete(SLnode(40, "kite"))
    for i in range(0, SL.getHeight()):
        SL.S[i].print_List()

    print("Insert (27, eric)")
    SL.insert(SLnode(27, "eric"))
    for i in range(0, SL.getHeight()):
        SL.S[i].print_List()

    print("delete (45, lisa)")
    SL.delete(SLnode(45, "lisa"))
    for i in range(0, SL.getHeight()):
        SL.S[i].print_List()

    print("delete (27, luis)")
    SL.delete(SLnode(27, "luis"))
    for i in range(0, SL.getHeight()):
        SL.S[i].print_List()

    print("delete (8, kids)")
    SL.delete(SLnode(8, "kids"))
    for i in range(0, SL.getHeight()):
        SL.S[i].print_List()

    print("delete (88, luke)")
    SL.delete(SLnode(88, "luke"))
    for i in range(0, SL.getHeight()):
        SL.S[i].print_List()

    return


print(read_lines())
print('-----------------------------------------------')
create_SkipLists()
