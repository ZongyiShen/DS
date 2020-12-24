class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None  # smaller
        self.right_child = None  # greater


class Binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # 判斷tree是否為空
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)

        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)

        # value == cur_node.value
        else:
            print("This value has existed")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)


def inorder(r):
    return inorder(r.left_child)+[r.value]+inorder(r.right_child) if r else []


def main():
    tree1 = Binary_search_tree()
    tree1.insert(10)
    tree1._insert(5, tree1.root)
    tree1._insert(15, tree1.root)
    tree1._insert(3, tree1.root)
    tree1._insert(8, tree1.root)
    tree1._insert(13, tree1.root)
    tree1._insert(18, tree1.root)
    tree1._insert(1, tree1.root)
    # tree1.print_tree()
    print(inorder(tree1.root))


main()
