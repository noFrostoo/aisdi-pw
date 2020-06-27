from binarytree import btstree_creation_time, btstree_search_time
from avltree import avltree_creation_time, avltree_search_time
from time_trees import draw_plot, time_tree, draw_plot_s, time_tree_search
from numpy import random
import sys


def main():
    sys.setrecursionlimit(20000)  # setting new limit so get_heightch can work
    crfile = open("rawcome.txt", 'w')
    srfile = open("rawcome-s.txt", 'w')
    outfile = open("outcome.txt", 'w')
    y_axis = []
    y_axis_s = []
    x_axis_c = [500, 1000, 2000, 3000, 5000, 7500, 10000]
    x_axis_s = range(1, 10000)
    numbers = list(random.randint(low=1, high=5000, size=10000))
    functions_create = [btstree_creation_time, avltree_creation_time]
    functions_search = [btstree_search_time, avltree_search_time]
    func_name = ['BTS creation time', 'Avl Creation Time',
                 'BTS search time', 'AVl search time']
    i = 0
    for func in functions_create:
        print(f'{func_name[i]}')
        outfile.write(f'{func_name[i]}')
        y, info = time_tree(func, numbers, x_axis_c)
        y_axis.append(y)
        draw_plot(x_axis_c, y, func_name[i], 'm', func_name[i])
        i += 1
        outfile.writelines(info)
    for func in functions_search:
        print(f'{func_name[i]}')
        outfile.write(f'{func_name[i]}')
        y, info = time_tree_search(func, numbers)
        y_axis_s.append(y)
        draw_plot_s(x_axis_s, y, func_name[i], 'm', func_name[i])
        i += 1
        outfile.writelines(info)
    crfile.write(f'{y_axis_s}')
    srfile.write(f'{y_axis}')


if __name__ == "__main__":
    main()
