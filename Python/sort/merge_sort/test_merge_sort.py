#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge sort test module"""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, param

from iterative_merge_sort import iter_merge_sort as isort
from recursive_merge_sort import rec_merge_sort as rsort


# pylint: disable=arguments-out-of-order


@mark.parametrize("seq, res", [([], []), ("", []), ((), [])])
def test_empty_sequences(seq, res):
    """Empty sequences."""
    assert isort(seq) == res
    assert rsort(seq) == res


@mark.parametrize("seq", [[1], "1", (1,)])
def test_single_element_sequence(seq):
    """Single element sequences."""
    res = list(seq)
    assert isort(seq) == res
    assert rsort(seq) == res


@mark.parametrize("seq", [[-1, 1], (-2, 0, 2), "ABCxyz", "1234567"])
def test_sorted_sequences(seq):
    """Sorted sequences."""
    res = list(seq)
    assert isort(seq) == res
    assert rsort(seq) == res


@mark.parametrize("seq", [[1, 0], (2, -2, 0), "qwerty", "School42"])
def test_unsorted_sequences(seq):
    """Unsorted sequences."""
    res = sorted(seq)
    assert isort(seq) == res
    assert rsort(seq) == res


@mark.parametrize(
    "nonseq", [param(42, marks=mark.xfail), param(None, marks=mark.xfail)]
)
def test_nonsequences(nonseq):
    """Non-sequences."""
    assert isort(nonseq)
    assert rsort(nonseq)
