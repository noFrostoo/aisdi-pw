from naive import naive_time
from knp import knp_time
from time_pattters import time_pattern, draw_plot, draw_plots, load_words, get_words_amount


def main():
    rfile = open("rawcome.txt", 'w')
    outfile = open("outcome.txt", 'w')
    y_axis = []
    x_axis = get_words_amount()
    functions = [naive_time, knp_time]
    func_name = ['Algorytm naiwny ', 'Algorytm KNP']
    words = load_words(20000)
    i = 0
    for fun in functions:
        print(f'{func_name[i]}')
        outfile.write(f'{func_name[i]}')
        y, info = time_pattern(fun, words)
        y_axis.append(y)
        draw_plot(x_axis, y, func_name[i], 'm', func_name[i])
        i += 1
        outfile.writelines(info)
    rfile.write(f'{y_axis}')
    draw_plots(x_axis, y_axis, func_name, ["m", "b", "g"])


if __name__ == "__main__":
    main()
