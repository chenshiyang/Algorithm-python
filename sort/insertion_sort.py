def insertionSort(array):
    if array is None or len(array) <= 1:
        return array
    for i in range(1, len(array), 1):
        j = i - 1
        temp = array[i]
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array

if __name__ == '__main__':
    array = [5, 3, 4, 9, 1]
    print(insertionSort(array))
    print(insertionSort(None))
    print(insertionSort([1]))
