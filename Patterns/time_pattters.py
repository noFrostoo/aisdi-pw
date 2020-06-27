from matplotlib import pyplot as plt


def time_pattern(func, numbers):
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
    filename = 'pan-tadeusz.txt'
    with open(filename, encoding='utf-8') as tadek:
        data = tadek.read()
        data = clear_new_line(data)
    for amount in words_a:
        time = func(amount, data)
        times.append(time)
        info = f'Amount: {amount}, Time: {time}'
        print(info)
        info_form_screen.append(info)
    return times, info_form_screen


def get_words_amount():
    return [x for x in range(1, 1000, 100)]


def draw_plot(x_axis, y_axis_l, label, color, func_name):
    plt.clf()
    plt.plot(x_axis, y_axis_l, label=label, color=color)
    plt.tight_layout()
    plt.legend()
    plt.grid(True)
    plt.title(f'{func_name}')
    plt.xlabel("Ilość słow")
    plt.ylabel("Czas wyszukiwania całkowity[s]")
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
    plt.title(f'Wyszukiwanie wzorca')
    plt.xlabel("Ilość słow")
    plt.ylabel("Czas wyszukiwania całkowity[s]")
    plt.show()
    input()
    plt.savefig(f'all.png')


def load_words(amount):
    """
    Functions loads word from pan-tadeusz.txt

    Args:
        amount(int) - how many words to load

    Return:
        list- loaded words in a list
    """
    filename = 'pan-tadeusz.txt'
    added = 0
    exit_list = []
    with open(filename, encoding='utf-8') as tadek:
        data = tadek.readlines()
        for line in data:
            if line == '\n':
                continue
            splitted = line[:len(line)-1].split(" ")
            # shorter line cuz, last char is new line char
            for word in splitted:
                if added == amount:
                    break
                exit_list.append(word)
                added += 1
    return exit_list


def clear_new_line(data):
    exitstr = ''
    for c in data:
        if c != '\n':
            exitstr += c
    return exitstr