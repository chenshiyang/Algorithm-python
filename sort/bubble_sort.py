def bubbleSort(array):
    if array is None or len(array) <= 1:
        return array
    for i in range(len(array)):
        for j in range(len(array) - 1, i, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
    return array

if __name__ == '__main__':
    array = [5, 3, 4, 9, 1]
    print(bubbleSort(array))
    print(bubbleSort(None))
    print(bubbleSort([1]))