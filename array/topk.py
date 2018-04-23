def buildMaxHeap(array):
    for i in range(int(len(array) / 2), -1, -1):
        heapify(array, i, len(array))


def heapify(heap, rootIdx, size):
    left = rootIdx * 2 + 1
    right = rootIdx * 2 + 2
    largest = rootIdx
    if left < size and heap[left] > heap[largest]:
        largest = left
    if right < size and heap[right] > heap[largest]:
        largest = right
    if largest != rootIdx:
        heap[rootIdx], heap[largest] = heap[largest], heap[rootIdx]
        heapify(heap, largest, size)

def getTopK(array, k):
    buildMaxHeap(array)
    print(array)
    size = len(array)
    result = []
    for i in range(k):
        result.append(array[0])
        array[0], array[size - 1] = array[size - 1], array[0]
        size -= 1
        heapify(array, 0, size)
    return result

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    topk = getTopK(array, 9)
    print(topk)