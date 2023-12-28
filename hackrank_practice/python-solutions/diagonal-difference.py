def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0

    for i in range(len(arr)):
        left_to_right += arr[i][i]

    for i in range(len(arr)):
        right_to_left += arr[i][(len(arr) - 1) - i]

    return abs(left_to_right - right_to_left)


# This problem wanted me to add the diagonals of a matrix
# and return the absolute value of the difference between the two.
