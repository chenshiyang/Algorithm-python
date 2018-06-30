def countNumberOfInversion(array):
    '''
    计算给定数组中逆序对的数量

    思路：对归并排序做一点修改, 在归并时统计逆序对的数量

    :param array:
    :return:
    '''
    if array is None or len(array) <= 1:
        return 0
    number = [0]
    doCount(array, 0, len(array) - 1, number)  # 为了便于传值, 所以定义一个长度为1的list
    return number[0]


def doCount(array, start, end, number):
    if end <= start:
        return
    mid = start + (end - start) // 2
    doCount(array, start, mid, number)
    doCount(array, mid + 1, end, number)
    merge(array, start, mid, end, number)


def merge(array, start, mid, end, number):
    temp = [0] * (end - start + 1)
    i = start
    j = mid + 1
    k = 0
    while i <= mid or j <= end:
        if i > mid:
            temp[k] = array[j]
            k += 1
            j += 1
        elif j > end:
            temp[k] = array[i]
            k += 1
            i += 1
        else:
            if array[i] <= array[j]:
                temp[k] = array[i]
                k += 1
                i += 1
            else:
                temp[k] += array[j]
                number[0] += (mid - i + 1)  # 前半部分剩余的元素 都可以和array[j]构成逆序对
                k += 1
                j += 1
    for i in range(len(temp)):
        array[start + i] = temp[i]


if __name__ == '__main__':
    array1 = [1, 2, 3, 7, 4, 6]
    print(countNumberOfInversion(array1))
    array2 = [2, 4, 1, 3, 5]
    print(countNumberOfInversion(array2))
