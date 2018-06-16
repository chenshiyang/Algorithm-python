def longestIncreasingSubsequence(array):
    '''
    nlogn 最长增长子序列
    :param array:
    :return:
    '''
    if array is None or len(array) == 0:
        return 0
    # minLength[i]表示长度为i的增长子序列的最后一个元素的最小值
    # minLength[0]不用
    minLength = [0] * (len(array) + 1)
    #len表示最长增长子序列的长度,初始化为1
    length = 1
    # 长度为1的增长子序列的最后一个元素初始化为array[0]
    minLength[1] = array[0]
    for i in range(1, len(array)):
        if array[i] > minLength[length]:
            length += 1
            minLength[length] = array[i]
        else:
            pos = binarySearch(minLength, 1, length, array[i])
            minLength[pos] = array[i]

    print(minLength)
    return length

def binarySearch(array, l, r, target):
    while l <= r:
        mid = int(l + (r - l) / 2)
        if array[mid] > target:
            r = mid - 1
        elif array[mid] < target:
            l = mid + 1
        else:
            return mid + 1#如果array[mid]==target,那么target应该插入其后面一个位置
    return l

if __name__ == '__main__':
    array1 = [1, 2, 3, 2]
    print(longestIncreasingSubsequence(array1))