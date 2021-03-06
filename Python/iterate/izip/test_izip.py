#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Izip test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import fixture

from izip import izip


# pylint: disable=redefined-outer-name


@fixture()
def iterables():
    """Iterables for izip."""
    return [[], [0], [1, 0], [-1, 0, 1], "hello", (None, [None], {None})]


def test_iterables(iterables):
    """Zip several test cases."""
    for it1 in iterables:
        for it2 in iterables:
            assert list(izip(it1, it2)) == list(zip(it1, it2))
