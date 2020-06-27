from binheap import bin_heap_time
from threedarr import d3_heap_time
from fourHeap import d4_heap_time
from time_heaps import get_words_amount, draw_plot, time_heap, draw_plots
from numpy import random


def main():
    rfile = open("rawcome.txt", 'w')
    outfile = open("outcome.txt", 'w')
    y_axis = []
    x_axis = get_words_amount()
    functions = [bin_heap_time, d3_heap_time, d4_heap_time]
    func_name = ['Kopiec 2-arny', 'Kopiec 3-arny', 'Kopiec 4-arny']
    numbers = list(random.randint(low=1, high=100000, size=51000))
    i = 0
    for fun in functions:
        print(f'{func_name[i]}')
        outfile.write(f'{func_name[i]}')
        y, info = time_heap(fun, numbers)
        y_axis.append(y)
        draw_plot(x_axis, y, func_name[i], 'm', func_name[i])
        i += 1
        outfile.writelines(info)
    rfile.write(f'{y_axis}')
    draw_plots(x_axis, y_axis, func_name, ["m", "b", "g"])


if __name__ == "__main__":
    main()
