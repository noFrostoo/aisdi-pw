from timeit import timeit


class Min3DHeap:
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
        return (position-1)//3

    def get_children(self, position):
        """
        Returns list with indexes of childer of given index
        Childern are located under 3*parentpos + i where i is 1 to 3
        Args:
            positions(int) - pos of an item
        Returns
            list- list with chidren
        """
        exit_list = []
        for i in range(1, 4):
            if (3*position+i) < self.size:
                exit_list.append(3*position+i)
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
        for i in range(0, self.size//3):
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


def d3_heap_time(given_list):
    setupcode = '''
from threedarr import Min3DHeap
    '''
    MYSTML = f'Min3DHeap({given_list})'
    return timeit(setup=setupcode, stmt=MYSTML, number=100)
