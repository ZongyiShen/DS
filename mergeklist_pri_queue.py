from queue import PriorityQueue
import heapq


class ListNode:
    def __init__(self, data, next=None):
        self.val = data
        self.next = next


def make_list(elements):
    head = now = ListNode(elements[0])
    for i in range(1, len(elements)):
        now.next = ListNode(elements[i])
        now = now.next
    return head


def print_list(head):
    now = head
    while(now != None):
        print(now.val)
        now = now.next


def linklist_to_array(head):
    a = []
    now = head
    while(now != None):
        a.append(now.val)
        now = now.next
    return a


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        '''
        i = 0
        for l in lists:
            if l:
                q.put((l.val, i, l))
                i += 1
        '''
        for index, l in enumerate(lists):
            if l:
                q.put((l.val, index, l))
        while not q.empty():
            val, index, node = q.get()  # cost O(logk)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, index, node))  # cost O(logk)
        return head.next


ob = Solution()
lists = [[1, 4, 5], [1, 3, 6], [7, 8]]
lls = []
for ll in lists:
    l = make_list(ll)
    lls.append(l)
print_list(ob.mergeKLists(lls))
a = linklist_to_array(ob.mergeKLists(lls))
print(a)
