"""List tests."""

import sys
from lists import (DLList, keep, reverse, sort)

def make_doubly_linked_lists(): 
    a = DLList([5])
    b = DLList([1, 2, 3, 4, 5])
    c = DLList([10, 4, 8, 3, 1, 2])
    d = DLList([1, 1, 1, 1, 1, 1])
    
    return a, b, c, d

def test_keep(capsys):
    a, b, c, d = make_doubly_linked_lists()
    keep(b, lambda a: a % 2 == 0)
    print(b) 
    out, err = capsys.readouterr()
    assert out == "[2, 4]\n"

    keep(d, lambda a: a % 2 == 0)
    print(d) 
    out, err = capsys.readouterr()
    assert out == "[]\n"

    keep(c, lambda a: a == 8)
    print(c) 
    out, err = capsys.readouterr()
    assert out == "[8]\n"

def test_reverse(capsys):
    a, b, c, d = make_doubly_linked_lists()
    reverse(b)
    print(b) 
    out, err = capsys.readouterr()
    assert out == "[5, 4, 3, 2, 1]\n"

    reverse(c)
    print(c) 
    out, err = capsys.readouterr()
    assert out == "[2, 1, 3, 8, 4, 10]\n"

    reverse(a)
    print(a)
    out, err = capsys.readouterr()
    assert out == "[5]\n"


def test_sort(capsys):
    a, b, c, d = make_doubly_linked_lists()


    x = DLList([1, 3, 12, 6, 4, 5])
    sort(x)
    print(x)
    out, err = capsys.readouterr()
    assert out == "[1, 3, 4, 5, 6, 12]\n"

    sort(a)
    print(a)
    out, err = capsys.readouterr()
    assert out == "[5]\n"

    sort(b)
    print(b)
    out, err = capsys.readouterr()
    assert out == "[1, 2, 3, 4, 5]\n"