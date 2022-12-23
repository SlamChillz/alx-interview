#!/usr/bin/python3
"""
Defines a pascal triangle function
"""


def pascal_triangle(n):
    """
    Args:
        n (integer): triangle height
    Returns:
        list of lists of integers
    """
    if n <= 0:
        return []
    pascal = []
    for _ in range(n):
        if len(pascal) == 0:
            pascal.append(line([]))
        else:
            pascal.append(line(pascal[-1]))
    return pascal


def line(prev):
    """
    Calculates the values of the next line
    Args:
        prev (list): a list of integers
    Returns:
        list of integers
    """
    if prev == []:
        return [1]
    length = len(prev)
    newLine = []
    for v in range(length):
        if v != length - 1:
            newLine.append(prev[v] + prev[v+1])
    return [prev[0]] + newLine + [prev[-1]]
