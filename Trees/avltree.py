from binarytree import Node
from timeit import timeit
import sys

sys.setrecursionlimit(20000)  # sets recursion to make sure big trees dosen't
# have a problem with reccursion in pytohn


class AvlTree:
    def __init__(self, num_list):
        self.__root = Node(num_list[0])
        for num in num_list[1:]:
            self.AVLinsert(num)

    def rebalance(self, balance, key, node):
        """
        performs rebalance if needed
        args:
            balance - int with current balance
            key - current key
            node - node to rebalance
        returns:
            node - new or old node
        """
        if balance > 1:
            if key < node.left.value:
                return self.rightRotate(node)
            if key > node.left.value:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
        if balance < -1:
            if key > node.right.value:
                return self.leftRotate(node)
            if key < node.right.value:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)

        return node

    def leftRotate(self, node):
        """
        left rotation
        args:
            node - node to prefrom rotation
        retuns:
            node - new node after rotation
        """
        new_node = node.right
        templ = new_node.left

        new_node.left = node
        node.right = templ

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        new_node.height = 1 + max(self.get_height(new_node.left),
                                  self.get_height(new_node.right))
        # Return the new node
        return new_node

    def rightRotate(self, node):
        """
        right rotation
        args:
            node - node to prefrom rotation
        retuns:
            node - new node after rotation
        """
        new_node = node.left
        tempr = new_node.right

        new_node.right = node
        node.left = tempr

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        new_node.height = 1 + max(self.get_height(new_node.left),
                                  self.get_height(new_node.right))

        # Return the new node
        return new_node

    def _AVLinsert(self, node, key):
        """
        Insert methode - inserts node into tree, if key is a duplicate
        intreases counter, inestion rules as avl, pertforms rebalance
        if needed
        Args:
            value - value to inster
            node - node to start insert from
        returns:
            node - new node as node given
        """
        if key == node.value:
            node.counter = key
            return node
        elif key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                node.left = self._AVLinsert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                node.right = self._AVLinsert(node.right, key)

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        balance = self.get_balance(node)

        node = self.rebalance(balance, key, node)
        return node

    def AVLinsert(self, key):
        """
        inster methode - uses private insert and changes root if needed
        Args:
            key - key  to insert
        Returns:
            nothing
        """
        self.__root = self._AVLinsert(self.__root, key)

    def pre_order_list(self):
        """
        pre order traversal - node, left, right
        Args:
            node - node to start traversal from
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

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        """
        returns balnce - it means divrence between left height and right height
        args:
            node - node to get balance from
        returns:
            balance - int
        """
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def search(self, key):
        """
        Search methode - uses search  root's node function
        Args:
            key - value to find
        returns:
            node with that value
        """
        return self.__root.search(key)


def avltree_creation_time(numbers):
    setupcode = '''
from avltree import AvlTree
    '''
    MYSTML = f'AvlTree({numbers})'
    return timeit(setup=setupcode, stmt=MYSTML, number=100)


def avltree_search_time(numbers):
    times = []
    setupcode = f'from avltree import AvlTree\navl = AvlTree({numbers})'
    for i in range(1, 10000):
        MYSTML = f'avl.search({numbers[i]})'
        times.append(timeit(setup=setupcode, stmt=MYSTML, number=10))
    return times
