def selectionSort(array):
    if array is None or len(array) <= 1:
        return array
    for i in range(len(array)):
        minIdx = i
        for j in range(i + 1, len(array), 1):
            minIdx = j if array[j] < array[minIdx] else minIdx
        array[i], array[minIdx] = array[minIdx], array[i]
    return array

if __name__ == '__main__':
    array = [5, 3, 4, 9, 1]
    print(selectionSort(array))
    print(selectionSort(None))
    print(selectionSort([1]))
