from naive import naive
from knp import kmp_matcher, compute_prefix_functions
from random import choice


def test_prefix_functions():
    assert [0, 0, 1, 2, 3, 0, 1] == compute_prefix_functions("ababaca")


def test_1():
    assert [1] == naive("abba", "aabbaa")
    assert [1] == kmp_matcher("abba", "aabbaa")


def test_2():
    assert [1, 5] == naive("abba", "aabbaabbaa")
    assert [1, 5] == kmp_matcher("abba", "aabbaabbaa")


def test_3():
    assert [0, 1, 2, 3, 4, 5] == naive("a", "aaaaaab")
    assert [0, 1, 2, 3, 4, 5] == kmp_matcher("a", "aaaaaab")


def test_4():
    assert [] == naive("", "aaaaaa")
    assert [] == kmp_matcher("", "aaaaaa")


def test_5():
    assert [0] == naive("abba", "abba")
    assert [0] == kmp_matcher("abba", "abba")


def test_6():
    assert [] == naive("aaaaaaaa", "aaaa")
    assert [] == kmp_matcher("aaaaaaaa", "aaaa")


def test_7():
    assert [0, 9, 13] == naive("AABA", "AABAACAADAABAAABAA")
    assert [0, 9, 13] == kmp_matcher("AABA", "AABAACAADAABAAABAA")


def test_random():
    a = ['a', 'b']
    pattern = ''
    text = ''
    for i11 in range(200):
        for i11 in range(10):
            pattern += choice(a)
        for i22 in range(100):
            text += choice(a)
        assert naive(pattern, text) == kmp_matcher(pattern, text)


def test_random_2():
    a = ['a', 'b', 'c']
    pattern = ''
    text = ''
    for i12 in range(200):
        pattern += choice(a)
    for i21 in range(100):
        text += choice(a)
    assert naive(pattern, text) == kmp_matcher(pattern, text)
