def quickSort(array):
    if array is None or len(array) <= 1:
        return array
    partition(array, 0, len(array) - 1)

def partition(array, start, end):
    if end <= start:
        return
    pivot = getPivot(array, start, end)
    i = start + 1;
    while i <= end and array[i] <= array[pivot]:
        i += 1
    j = i
    while j <= end:
        if array[j] < array[pivot]:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    array[pivot], array[i - 1] = array[i - 1], array[pivot]
    partition(array, start, i - 2)
    partition(array, i, end)


def getPivot(array, i, j):
    return i

if __name__ == '__main__':
    array = [5, 3, 4, 9, 1]
    quickSort(array)
    print(array)