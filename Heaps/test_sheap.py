from binheap import Min2DHeap
from threedarr import Min3DHeap
from fourHeap import Min4DHeap
import numpy as np


def test_bin_heap_1():
    Heapbin = Min2DHeap([15, 4, 3, 17, 10, 20, 19, 6, 22, 9])
    assert [3, 6, 4, 10, 9, 20, 19, 17, 22, 15] == Heapbin.items
    assert [3, 6, 4, 6, 10, 9, 4, 20, 19, 10, 17, 22, 9,
            15, 20, 19, 17, 22, 15] == Heapbin.print_heap_pre_order()


def test_bin_heap_2():
    Heapbin = Min2DHeap([15, 4, 3, 17, 10, 20, 19, 6, 22, 9])
    assert Heapbin.extract_min() == 3
    assert [4, 6, 15, 10, 9, 20, 19, 17, 22] == Heapbin.items


def test_2d_heap_rand():
    for i in range(100):
        numbers = np.random.randint(1, 1000, 100)
        Heapbin = Min2DHeap(numbers)
        assert min(numbers) == Heapbin.items[0]
        assert min(numbers) == Heapbin.get_min()


def test_3d_heap_1():
    Heapbin = Min3DHeap([4, 5, 6, 7, 8, 9, 10, 3])
    assert [3, 5, 4, 7, 8, 9, 10, 6] == Heapbin.items


def test_3d_heap_2():
    Heapbin = Min3DHeap([12, 14, 15, 13, 11, 10, 18])
    assert [10, 11, 15, 13, 14, 12, 18] == Heapbin.items


def test_3d_heap_rand():
    for i in range(100):
        numbers = np.random.randint(1, 1000, 100)
        Heapbin = Min3DHeap(numbers)
        assert min(numbers) == Heapbin.items[0]
        assert min(numbers) == Heapbin.get_min()


def test_4d_heap_1():
    Heapbin = Min4DHeap([15, 4, 3, 17, 10, 20, 19, 6, 22, 9])
    assert [3, 6, 4, 17, 10, 20, 19, 15, 22, 9] == Heapbin.items


def test_4d_heap_rand():
    for i in range(100):
        numbers = np.random.randint(1, 1000, 100)
        Heapbin = Min4DHeap(numbers)
        assert min(numbers) == Heapbin.items[0]
        assert min(numbers) == Heapbin.get_min()
