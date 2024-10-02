#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    a function that returns a list
    of integers representing the
    pascal triangle of n:
       . Returns an empty list if n <= 0
       . assume n will be always an integer
    """
    Pascal = []

    if n <= 0:
        return []

    for x in range(n):
        if (x == 0):
            Pascal.append([1])
        else:
            Current_row = []
            for y in range(x + 1):
                if (y == 0 or y == x):
                    Current_row.append(1)
                else:
                    Current_row.append(Pascal[x - 1][y - 1] + Pascal[y - 1][y])

            Pascal.append(Current_row)

    return (Pascal)
