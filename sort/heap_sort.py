def heapSort(array):
    '''
    小顶堆实现倒序排序,
    若要正序排序,需要使用大顶堆
    :param array:
    :return:
    '''
    if array is None or len(array) <= 1:
        return array
    buildHeap(array)
    for size in range(len(array), 0, -1):
        array[size - 1], array[0] = array[0], array[size - 1]
        heapify(array, 0, size)
    return array


def heapify(array, rootIndex, size):
    left = rootIndex * 2 + 1
    right = rootIndex * 2 + 2
    largest = rootIndex
    if left < size and array[left] > array[largest]:
        largest = left
    if right < size and array[right] > array[largest]:
        largest = right
    if largest != rootIndex:
        array[largest], array[rootIndex] = array[rootIndex], array[largest]
        heapify(array, largest, size)

def buildHeap(array):
    size = len(array)
    for i in range(int(size / 2), -1, -1):
        heapify(array, i, size)

if __name__ == '__main__':
    array = [5, 3, 4, 9, 1]
    print(heapSort(array))
    print(heapSort(None))
    print(heapSort([1]))