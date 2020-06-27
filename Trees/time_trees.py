from numpy import random
from matplotlib import pyplot as plt
import sys

sys.setrecursionlimit(10000)


def time_tree(func, numbers, x_axis):
    times = []
    info_form_screen = []
    for i in x_axis:
        time = func(numbers[:i+1])
        times.append(time)
        info = f'Amount: {len(numbers[:i+1])}, Time: {time}'
        print(info)
        info_form_screen.append(info)
    return times, info_form_screen


def time_tree_search(func, numbers):
    times = []
    info_form_screen = []
    times = func(numbers)
    info = f"1000 number from list took {times[0]} to find"
    print(info)
    info_form_screen.append(info)
    return times, info_form_screen


def draw_plot(x_axis, y_axis_l, label, color, func_name):
    plt.clf()
    plt.plot(x_axis, y_axis_l, label=label, color=color)
    plt.tight_layout()
    plt.legend()
    plt.grid(True)
    plt.title(f'{func_name}')
    plt.xlabel("Amount of numbers")
    plt.ylabel("Time in s")
    plt.savefig(f'{func_name}.png')


def draw_plot_s(x_axis, y_axis_l, label, color, func_name):
    plt.clf()
    plt.plot(x_axis, y_axis_l, label=label, color=color)
    plt.tight_layout()
    plt.legend()
    plt.grid(True)
    plt.title(f'{func_name}')
    plt.xlabel("Index of number in list")
    plt.ylabel("Time in s")
    plt.savefig(f'{func_name}.png')


def generate_numbers(amounts):
    nums = []
    for amount in amounts:
        nums.append(random.randint(low=1, high=5000, size=amount))
    return nums
