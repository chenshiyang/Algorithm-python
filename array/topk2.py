def heapify(array, rootIdx, size):
    left = rootIdx * 2 + 1
    right = rootIdx * 2 + 2
    smallest = rootIdx
    if left < size and array[left] < array[smallest]:
        smallest = left
    if right < size and array[right] < array[smallest]:
        smallest = right
    if smallest != rootIdx:
        array[rootIdx], array[smallest] = array[smallest], array[rootIdx]
        heapify(array, smallest, size)

def buildHeap(array):
    '''
    初始化一个小顶堆，时间复杂度O(n)
    :param array:
    :return:
    '''
    for i in range(len(array), -1, -1):
        heapify(array, i, len(array))

def topk(array, k):
    '''
    获取一个列表中的前k大个元素
    总时间复杂度为：O(k) + (n-k)logk + klogk(最后若排序的话)=O(nlogk)
    :param array:
    :param k:
    :return:
    '''
    heap = array[:k]
    buildHeap(heap)
    for i in range(k, len(array), 1):
        temp = array[i]
        if temp > heap[0]:
            heap[0] = temp
            heapify(heap, 0, len(heap))
    #如果需要获得的k个元素是有序的，则对这k个元素再排序一次，复杂度为klog(k)
    return sorted(heap, reverse=True)
    # return heap

if __name__ == '__main__':
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(topk(array, 8))