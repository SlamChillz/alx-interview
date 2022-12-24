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
    pascal = [[1]]
    for _ in range(1, n):
        pascal.append(line(pascal[-1]))
    return pascal


def line(prev):
    """
    Calculates the values of the next line
    Args:
        prev (list): previous list of integers
    Returns:
        next list of integers
    """
    length = len(prev)
    newLine = []
    for v in range(length - 1):
        newLine.append(prev[v] + prev[v+1])
    return [prev[0]] + newLine + [prev[-1]]
