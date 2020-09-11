"""
find minimum number of steps taken from point a to b. through points that lie in between.
array x_arr & y_arr store the respective x and y co-ordinates of points.
"""


def cover_points(x_arr, y_arr):
    count = 0
    for i in range(1, len(x_arr)):
        count += max(abs(x_arr[i] - x_arr[i - 1]), abs(y_arr[i] - y_arr[i - 1]))
    return count
