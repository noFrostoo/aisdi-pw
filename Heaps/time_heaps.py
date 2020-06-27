from matplotlib import pyplot as plt


def time_heap(func, numbers):
    """
    Function times of building heap
    Args:
        func - function to time
    Return:
        tuple - list with raw times and formated info from screen
    """
    times = []
    info_form_screen = []
    words_a = get_words_amount()
    for amount in words_a:
        to_build = numbers[:amount]
        time = func(to_build)
        times.append(time)
        info = f'Amount: {amount}, Time: {time}'
        print(info)
        info_form_screen.append(info)
    return times, info_form_screen


def get_words_amount():
    return [x for x in range(100, 50000, 500)]


def draw_plot(x_axis, y_axis_l, label, color, func_name):
    plt.clf()
    plt.plot(x_axis, y_axis_l, label=label, color=color)
    plt.tight_layout()
    plt.legend()
    plt.grid(True)
    plt.title(f'{func_name}')
    plt.xlabel("Ilość liczb")
    plt.ylabel("Czas budowanie kopca[s]")
    plt.show()
    input()
    plt.savefig(f'{func_name}.png')


def draw_plots(x_axis, y_axis_l, labels, colors):
    plt.clf()
    for i in range(3):
        plt.plot(x_axis, y_axis_l[i], label=labels[i], color=colors[i])
    plt.tight_layout()
    plt.legend()
    plt.grid(True)
    plt.title(f'Kopce')
    plt.xlabel("Ilość liczb")
    plt.ylabel("Czas budowanie kopców[s]")
    plt.show()
    input()
    plt.savefig(f'all.png')
