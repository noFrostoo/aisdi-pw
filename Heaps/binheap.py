from timeit import timeit


class Min2DHeap:
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

        if position == 0:
            return 0
        return (position-1)//2

    def get_left_child(self, position):
        """
        Returns position of left child of an item on given pos
        Args:
            positions(int) - pos of an item
        Returns
            int - pos of left child
        """
        if(position == 0):
            return 1
        if 2*position + 1 >= len(self.items):
            return False
        return 2*position + 1

    def get_right_child(self, position):
        """
        Returns position of right child of an item on given pos
        Args:
            positions(int) - pos of an item
        Returns
            int - pos of right child
        """
        if(position == 0):
            return 2
        if 2*position + 2 >= len(self.items):
            return False
        return (2*position) + 2

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

        while self.items[pos] < self.items[self.get_partent(pos)]:
            self.items[pos], self.items[
                self.get_partent(pos)] = self.items[
                    self.get_partent(pos)], self.items[pos]
            pos = self.get_partent(pos)

    def min_heapify(self, pos):
        """
        restores heap structure by swaping is a childer is smaler than parent
        from given pos
        Args:
            pos(int) - pos to start heapify from
        Returns
            nothing
        """
        if pos <= (self.size-1//2) and pos <= self.size:  # if not leaf
            if self.get_left_child(pos) and self.get_right_child(pos):
                if self.greater_than_any_child(pos):
                    if(self.items[self.get_right_child(pos)] > self.items[
                            self.get_left_child(pos)]):
                        self.swap(pos, self.get_left_child(pos))
                        self.min_heapify(self.get_left_child(pos))
                    else:
                        self.swap(pos, self.get_right_child(pos))
                        self.min_heapify(self.get_right_child(pos))

            elif self.get_right_child(pos):
                if self.items[pos] > self.items[self.get_right_child(pos)]:
                    self.swap(pos, self.get_right_child(pos))
                    self.min_heapify(self.get_right_child(pos))

            elif self.get_left_child(pos):
                if self.items[pos] > self.items[self.get_left_child(pos)]:
                    self.swap(pos, self.get_left_child(pos))
                    self.min_heapify(self.get_left_child(pos))

    def greater_than_any_child(self, pos):
        """
        returns true is node on positions(pos) is greater than any child
        used to improve readablity
        """
        return self.items[pos] > self.items[
                    self.get_left_child(pos)] or self.items[pos] > self.items[
                        self.get_right_child(pos)]

    def swap(self, pos1, pos2):
        """
        swaps two items in a list - used to reduce amount of code and improve
        readability
        """
        self.items[pos1], self.items[pos2] = self.items[pos2], self.items[pos1]

    def extract_min(self):
        """
        retuns min value from heap and restores heap stucture to the heap
        args:
            none
        returns:
            int - min value
        """
        number = self.items[0]
        self.items[0] = self.items[self.size-1]
        self.size -= 1
        self.items.pop()
        self.min_heapify(0)
        return number

    def get_min(self):
        return self.items[0]

    def print_heap_pre_order(self):
        exit_list = []
        for i in range(0, self.size):
            exit_list.append(self.items[i])
            if(self.get_left_child(i)):
                exit_list.append(self.items[self.get_left_child(i)])
            if self.get_right_child(i):
                exit_list.append(self.items[self.get_right_child(i)])
        return exit_list

    def print_heap_in_order(self):
        exit_list = []
        for i in range(1, self.size//2):
            if(self.get_left_child(i)):
                exit_list.append(self.items[self.get_left_child(i)])
            exit_list.append(self.items[i])
            if self.get_right_child(i):
                exit_list.append(self.items[self.get_right_child(i)])
        return exit_list

    def print(self):
        for i in range(0, self.size):
            print(f"Node: {self.items[i]},", end='')
            if self.get_left_child(i):
                print(f"Children:{self.items[self.get_left_child(i)]}", end="")
            if self.get_right_child(i):
                print(f", {self.items[self.get_right_child(i)]}", end="")
            print()


def bin_heap_time(given_list):
    setupcode = '''
from binheap import Min2DHeap
    '''
    MYSTML = f'Min2DHeap({given_list})'
    return timeit(setup=setupcode, stmt=MYSTML, number=100)


Heapbin = Min2DHeap([15, 4, 3, 17, 10, 20, 19, 6, 22, 9])
Heapbin.print()
