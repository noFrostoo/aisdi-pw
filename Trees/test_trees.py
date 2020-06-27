from binarytree import Tree, Node
from avltree import AvlTree


def compare_nodes(node1, node2):
    if node1.value == node2.value:
        if node1.left and node2.left:
            if node1.left.value == node2.left.value:
                if node2.right and node1.right:
                    if node1.right.value == node2.right.value:
                        return True
                    else:
                        return False
                else:
                    if node1.right is None and node2.right is None:
                        return True
                    return False
            else:
                return False
        else:
            if node1.left is None and node2.left is None:
                return True
            return False
    else:
        return False


def test_bts_1():
    numbers = [50, 30, 20, 40, 70, 60, 80]
    T = Tree(numbers)
    assert T.in_order_list() == [20, 30, 40, 50, 60, 70, 80]


def test_bts_2():
    numbers = [5, 6, 1, 10, 50, 30, 20, 40, 70, 60, 80]
    T = Tree(numbers)
    assert T.in_order_list() == sorted(numbers)


def test_bts_3():
    numbers = [50, 50, 50, 50, 30, 20, 40, 70, 60, 80]
    T = Tree(numbers)
    assert T.in_order_list() == [20, 30, 40, 50, 60, 70, 80]
    assert T.get_root().counter == 3


def test_bts_4():
    numbers = [50, 30, 20, 40, 70, 60, 80]
    T = Tree(numbers)
    assert T.pre_order_list() == numbers
    assert T.search(30).counter == 0


def test_bts_5():
    numbers = [50, 30, 30, 20, 40, 70, 60, 80]
    numbers_to_assert = [50, 30, 20, 40, 70, 60, 80]
    T = Tree(numbers)
    assert T.pre_order_list() == numbers_to_assert
    assert T.search(30).counter == 1


def test_avl_1():
    numbers = [10, 20, 30, 40, 50, 25]
    T = AvlTree(numbers)
    assert T.pre_order_list() == [30, 20, 10, 25, 40, 50]


def test_avl_2():
    numbers = [5, 6, 1, 10, 50, 30, 20, 40, 70, 60, 80]
    T = AvlTree(numbers)
    assert T.pre_order_list() == [10, 5, 1, 6, 50, 30, 20, 40, 70, 60, 80]


def test_avl_3():
    numbers = [5, 6, 1, 10, 50, 30, 20, 40, 70, 60, 80]
    T = AvlTree(numbers)
    assert T.in_order_list() == sorted(numbers)


def test_search_bts_1():
    numbers = [50, 30, 20, 40, 70, 60, 80]
    T = Tree(numbers)
    node = Node(50, Node(30), Node(70))
    assert T.search(50) == T.get_root()
    assert compare_nodes(T.search(50), node) is True


def test_search_bts_2():
    numbers = [50, 30, 20, 40, 70, 60, 80]
    T = Tree(numbers)
    node = Node(20)
    assert compare_nodes(T.search(20), node)


def test_search_bts_3():
    numbers = [50, 30, 20, 40, 70, 60, 80]
    T = Tree(numbers)
    node = Node(30, Node(20), Node(40))
    assert compare_nodes(T.search(30), node)


def test_search_avl_1():
    numbers = [10, 20, 30, 40, 50, 25]
    T = AvlTree(numbers)
    assert T.search(30) == T.get_root()


def test_search_avl_2():
    numbers = [10, 20, 30, 40, 50, 25]
    T = AvlTree(numbers)
    node = Node(20, Node(10), Node(25))
    assert compare_nodes(T.search(20), node)
