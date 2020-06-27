from timeit import timeit


class Min4DHeap:
    def __init__(self, given_list=[]):
        self.items = []
        self.size = 0
        for element in given_list:
            self.insert(element)

    def get_partent(self, position):
        """
        Returns position of parent of an item on given pos
        Args:
            positions(int) - pos of child
        Returns
            int - pos of parent
        """
        return (position-1)//4

    def get_children(self, position):
        """
        Returns list with indexes of childer of given index
        Childern are located under 4*parentpos + i where i is 1 to 4
        Args:
            positions(int) - pos of an item
        Returns
            list- list with chidren
        """
        exit_list = []
        for i in range(1, 5):
            if (4*position+i) < self.size:
                exit_list.append(4*position+i)
        return exit_list

    def insert(self, elemet):
        """
        Insets item to heap by appending to the list and then restoring heap
        structure by swaping as long as parent is smaller than child
        Args:
            element(int) - element to insert
        Returns
            nothing
        """
        self.items.append(elemet)
        pos = self.size
        self.size += 1
        while(pos > 0):
            if self.items[pos] < self.items[self.get_partent(pos)]:
                self.items[pos], self.items[
                    self.get_partent(pos)] = self.items[
                        self.get_partent(pos)], self.items[pos]
            else:
                break
            pos = self.get_partent(pos)

    def print_heap_pre_order(self):
        exit_list = []
        for i in range(1, self.size//3):
            exit_list.append(self.items[i])
            for c in self.get_children(i):
                exit_list.append(c)
        return exit_list

    def print(self):
        for i in range(0, self.size):
            print(f"Node: {self.items[i]},", end='')
            print(f"Children: ", end="")
            for c in self.get_children(i):
                print(f"{self.items[c]}, ", end='')
            print()

    def get_min(self):
        return self.items[0]


def d4_heap_time(given_list):
    setupcode = '''
from fourHeap import Min4DHeap
    '''
    MYSTML = f'Min4DHeap({given_list})'
    return timeit(setup=setupcode, stmt=MYSTML, number=100)


Heapbin = Min4DHeap([15, 4, 3, 17, 10, 20, 19, 6, 22, 9])
Heapbin.print()
