# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import itertools


def flippingMatrix(matrix):
    n = len(matrix[0])
    cuadrant_size = n // 2 - 1

    # for each column, make sure the largest number are at the top
    for col in range(n):
        max_num = matrix[0][col]
        idx = 0
        for row in range(n):
            if matrix[row][col] > max_num:
                max_num = matrix[row][col]
                idx = row

        # not in upper quadrant, flip column
        if idx > cuadrant_size:
            for row in range(n // 2):
                matrix[row][col], matrix[n - row - 1][col] = matrix[n - row - 1][col], matrix[row][col]

    # for each row, make sure the largest number are at the left
    for row in range(n):
        max_num = matrix[row][0]
        idx = 0
        for col in range(n):
            if matrix[row][col] > max_num:
                max_num = matrix[row][col]
                idx = col

        # not in upper quadrant, flip column
        if idx > cuadrant_size:
            for col in range(n // 2):
                matrix[row][col], matrix[row][n - col - 1] = matrix[row][n - col - 1], matrix[row][col]

    print(matrix)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = []
    print(flippingMatrix(matrix))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
