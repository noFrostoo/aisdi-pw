from timeit import timeit


def naive(string, text):
    positions = []
    n = len(text)
    m = len(string)

    if m == 0:
        return positions
    for i in range(n-m+1):
        s = 0
        while s < m:
            if text[i+s] != string[s]:
                break
            s += 1
        if s == m:
            positions.append(i)
    return positions


def naive_time(amount, data):
    setupcode = f'from naive import naive\nfrom time_pattters import load_words\nwords = load_words({amount})'
    MYSTML = f'for pattern in words:\n   naive(pattern, "{data}")'
    return timeit(setup=setupcode, stmt=MYSTML, number=1)


#naive("abba", "abba")