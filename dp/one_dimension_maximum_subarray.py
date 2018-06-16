def oneDimensionMaximumSubarray(array):
    if array is None or len(array) == 0:
        return None
    sum = array[0]
    maxSum = array[0]
    for i in range(1, len(array)):
        if sum > 0:
            sum += array[i]
        else:
            sum = array[i]
        maxSum = max(maxSum, sum)
    return maxSum

if __name__ == '__main__':
    array = [1, -2, 3, 1]
    print(oneDimensionMaximumSubarray(array))