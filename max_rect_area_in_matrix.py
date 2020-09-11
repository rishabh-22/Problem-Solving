# Finds the maximum area under the histogram represented
# by histogram. See below article for details.
# https:# www.geeksforgeeks.org / largest-rectangle-under-histogram

# Create an empty stack. The stack holds
# indexes of hist array / The bars stored
# in stack are always in increasing order
# of their heights.

def max_hist(row):
    result = []
    c = len(row)
    max_area = 0  # Initialize max area in current
    # row (or histogram)

    # Run through all bars of given
    # histogram (or row)
    i = 0
    while i < c:

        # If this bar is higher than the
        # bar on top stack, push it to stack
        if (len(result) == 0) or (row[result[0]] <= row[i]):
            result.append(i)
            i += 1
        else:
            top_val = row[result[0]]
            result.pop(0)
            area = top_val * i

            if len(result):
                area = top_val * (i - result[0] - 1)
            max_area = max(area, max_area)

            # Now pop the remaining bars from stack
    # and calculate area with every popped
    # bar as the smallest bar
    while len(result):
        top_val = row[result[0]]
        result.pop(0)
        area = top_val * i
        if len(result):
            area = top_val * (i - result[0] - 1)

        max_area = max(area, max_area)

    return max_area


# Returns area of the largest rectangle
# with all 1s in A
def max_rectangle(matrix):
    # Calculate area for first row and
    # initialize it as result

    # result = max_hist(matrix[0])
    result = 0

    # iterate over row to find maximum rectangular
    # area considering each row as histogram
    for i in range(1, len(matrix)):

        for j in range(len(matrix[i])):

            # if A[i][j] is 1 then add A[i -1][j]
            if matrix[i][j]:
                matrix[i][j] += matrix[i - 1][j]

                # Update result if area with current
        # row (as last row) of rectangle) is more
        result = max(result, max_hist(matrix[i]))

    return result


# Driver Code
if __name__ == '__main__':
    arr = [[0, 1, 1, 0],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 0, 0]]

    print("Area of maximum rectangle is", max_rectangle(arr))
