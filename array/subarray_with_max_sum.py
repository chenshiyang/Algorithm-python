def subarrayWithMaxSum(array):
    '''
    给定一个数组，求该数组的和最大的子数组
    :param array:
    :return:
    '''
    if array is None or len(array) == 0:
        return 0
    maxSum = array[0]
    #sum_array[i]表示以array[i]结尾的数组的最大和
    sum_array = [0] * len(array)
    sum_array[0] = array[0]
    l = 0
    r = 0
    new_l = 0
    for i in range(1, len(sum_array)):
        sum_array[i] = max(sum_array[i - 1] + array[i], array[i])
        if sum_array[i - 1] < 0:
            sum_array[i] = array[i]
            new_l = i
        else:
            sum_array[i] = sum_array[i - 1] + array[i]
        if sum_array[i] > maxSum:
            maxSum = sum_array[i]
            l = new_l
            r = i

    print(array[l: r + 1])
    return maxSum

if __name__ == '__main__':
    array = [4, -3, 5, 2, -20]
    print(subarrayWithMaxSum(array))
    array2 = [-5]
    print(subarrayWithMaxSum(array2))
    array3 = [-5, -6]
    print(subarrayWithMaxSum(array3))
    array4 = [-5, -6, 4]
    print(subarrayWithMaxSum(array4))
    array5 = [-5, -6, 4, 0, 1]
    print(subarrayWithMaxSum(array5))