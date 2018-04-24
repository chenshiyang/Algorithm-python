#coding:utf-8
def partition(array, left, right, k):
    if right - left < 1:
        return
    pivot = getPivot(array, left, right)
    pivotIdx = left
    i = pivotIdx + 1
    for j in range(i, right + 1, 1):
        if array[j] > array[pivotIdx]:#求topK 大用 >,求top k小用<
            array[j], array[i] = array[i], array[j]
            i += 1
    #after the for loop, array[i - 1] is the last element that smaller than array[pivotIdx]
    array[pivotIdx], array[i - 1] = array[i - 1], array[pivotIdx]
    if i == k:#因为前0-i-1个都是小于pivot的，所以如果如果i==k，则说明前0-i-1个刚好是前k个
        return
    if i < k:
        partition(array, i, right, k)
    else:
        partition(array, left, i - 2, k)


def getPivot(array, left, right):
    '''
    从数组中选择一个元素，作为划分基准，将这个元素放在array[left]中
    这里的默认实现，直接使用array[left]。
    也可以从[left, right]中随机得到一个index，然后swap(array[left],array[index])
    :param array:
    :param left:
    :param right:
    :return:
    '''
    return array[left]

def getTopk(array, k):
    partition(array, 0, len(array) - 1, k)
    return array[:k]

if __name__ == '__main__':
    array = [0, 2, 1, 6, 5, 4, 3, 8, 7, 9]
    print(getTopk(array, 3))

