from timeit import timeit


def compute_prefix_functions(string):
    m = len(string)
    if m == 0:
        return []
    pi = [0] * m
    pi[0] = 0
    k = 0
    q = 1
    if m <= 1:
        return pi
    for q in range(1, m):
        while k > 0 and string[k] != string[q]:
            k = pi[k-1]
        if string[k] == string[q]:
            k += 1
        pi[q] = k
    return pi


def kmp_matcher(string, text):
    n = len(text)
    m = len(string)
    if m == 0:
        return []
    pi = compute_prefix_functions(string)
    q = 0
    positions = []
    i = 0
    while i < n:
        while q > 0 and string[q] != text[i]:  # string [q] or q = -1
            q = pi[q-1]
        if string[q] == text[i]:
            q += 1
        if q == m:
            positions.append(i-(m-1))
            q = pi[q-1]
        i += 1
    return positions


def knp_time(amount, data):
    setupcode = f'from knp import kmp_matcher\nfrom time_pattters import load_words\nwords = load_words({amount})'
    MYSTML = f'for pattern in words:\n   kmp_matcher(pattern, "{data}")'
    return timeit(setup=setupcode, stmt=MYSTML, number=1)

# l = kmp_matcher("ababaca", "bacbababacacbab")
# print(l)

# kmp_matcher("", "bacbababacacbab")
print([x for x in range(18)])
print(compute_prefix_functions("AABA AAAB AABA AB"))