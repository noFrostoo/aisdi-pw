from timeit import timeit
import sys

sys.setrecursionlimit(10000)


class Node:
    """
    Mega Node - that incudes can be used like normal basic node but has
    traversal methodes, bts inster methode, varuios setters and search methode
    Paramtets:
        left - left node
        right - right node
        value - value of the node
        counter - amount of duplicas
        height - height of the node
    """
    def __init__(self, value, right=None, left=None, parent_node=None):
        self.__left = right
        self.__right = left
        self.__value = value
        self.__counter = 0
        self.__height = 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, he):
        self.__height = he

    @property
    def value(self):
        return self.__value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        if right is None:
            self.__right = right
        elif right.value == self.value:
            self.__counter += 1
        elif self.__value < right.value:
            self.__right = right
        else:
            print(f"Probabl not corret inserton:{self.__value}, {right.value}")

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        if left is None:
            self.__left = left
        elif left.value == self.value:
            self.__counter += 1
        elif self.__value > left.value:
            self.__left = left
        else:
            print(f"Probabl not corret inserton:{self.__value}, {left.value}")

    @property
    def counter(self):
        return self.__counter

    @counter.setter
    def counter(self, key):
        if self.__value == key:
            self.__counter += 1
        else:
            print("This is not a duplicate")

    def insert(self, value):
        """
        Insert methode - inserts node into tree, if key is a duplicate
        intreases counter, inestion rules as bts, does not pertform rebalance
        not avl methode, if cannot be interted returns false
        Args:
            value - value to inster
        returns:
            None or false - depends on succes
        """
        if self.__value == value:
            self.__counter += 1
        if self.__value:
            if value < self.__value:
                if self.__left is None:
                    self.left = Node(value)
                else:
                    self.__left.insert(value)
            elif value > self.__value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.__right.insert(value)
        else:
            self.__value = value

    def search(self, key):
        """
        Search methode - retuns node with given key
        args:
            key - node to find
        retyurn:
            node - node with key

        """
        if self.__value == key:
            return self
        elif self.__value < key:
            if self.right:
                return self.__right.search(key)
            else:
                return False
        else:
            if self.left:
                return self.__left.search(key)
            else:
                return False

    def get_height(self):
        if self.is_leaf():
            return 0
        self.__height = max(1+self.right.get_height(), self.left.get_height())
        return self.__height

    def is_leaf(self):
        """
        returns true if node is a leaf
        args:
            none
        Returns:
            bool
        """
        if self.__right or self.__left:
            return False
        return True

    def get_balance(self):
        """
        returns balnce - it means divrence between left height and right height
        args:
            none
        returns:
            balance - int
        """
        if self.is_leaf():
            return 0
        else:
            self.__balance = self.left.get_height() - self.right.get_height()
        return self.__balance

    def pre_order_list(self, node):
        """
        pre order traversal - node, left, right
        Args:
            node - node to start traversal from
        returns:
            list - list with values from tree
        """
        if not node:
            return []
        exit_l = [node.value]
        exit_l += self.pre_order_list(node.left)
        exit_l += self.pre_order_list(node.right)
        return exit_l

    def in_order_list(self, node):
        """
        in order traversal -  left, node, right
        Args:
            node - node to start traversal from
        returns:
            list - list with values from tree
        """
        if not node:
            return []
        exit_l = []
        exit_l += self.in_order_list(node.left)
        exit_l.append(node.value)
        exit_l += self.in_order_list(node.right)
        return exit_l


class Tree:
    """
    Bts tree - object is init by a list - first element is a root - class
    heavly on node class
    Paramets:
        root - roof of a tree

    """
    def __init__(self, num_list):
        self.__root = Node(num_list[0])
        for num in num_list[1:]:
            self.__root.insert(num)

    def search(self, key):
        """
        Search methode - uses search  root's node function
        Args:
            key - value to find
        returns:
            noode with that value
        """
        return self.__root.search(key)

    def insert(self, key):
        """
        Insert methode - uses insert  root's node function
        Args:
            key - value to inster
        returns:
            None
        """
        self.__root.insert(key)

    def get_height(self):
        return self.__root.get_height()

    def pre_order_list(self):
        """
        pre order traversal - node, left, right
        Args:
            nothing
        returns:
            list - list with values from tree
        """
        return self.__root.pre_order_list(self.__root)

    def in_order_list(self):
        """
        in order traversal -  left, node, right
        Args:
            node - node to start traversal from
        returns:
            list - list with values from tree
        """
        return self.__root.in_order_list(self.__root)

    def get_root(self):
        return self.__root


def btstree_creation_time(numbers):
    setupcode = '''
from binarytree import Tree
    '''
    MYSTML = f'Tree({numbers})'
    return timeit(setup=setupcode, stmt=MYSTML, number=100)


def btstree_search_time(numbers):
    times = []
    setupcode = f'from binarytree import Tree\nbts = Tree({numbers})'
    for i in range(1, 10000):
        MYSTML = f'bts.search({numbers[i]})'
        times.append(timeit(setup=setupcode, stmt=MYSTML, number=10))
    return times
