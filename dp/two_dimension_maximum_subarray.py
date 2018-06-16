def twoDimensionMaximumSubarray(array):
    if array is None or len(array) == 0:
        return 0
    maxSum = array[0][0]

    for low in range(len(array)):
        tempArray = [0 for j in range(len(array[0]))]
        for high in range(low, len(array)):
            # 将array[low,:]到array[high,:]的二维矩阵按列方向压缩成一维矩阵
            for k in range(len(tempArray)):
                tempArray[k] += array[high][k]
            # print(tempArray)
            maxSum = max(maxSum, oneDimensionMaximumSubarry(tempArray))
            # print("max sum is", maxSum)

    return maxSum

def oneDimensionMaximumSubarry(array):
    maxSum = array[0]
    sum = array[0]
    for i in range(1, len(array)):
        if sum > 0:
            sum += array[i]
        else:
            sum = array[i]
        maxSum = max(maxSum, sum)
    return maxSum

if __name__ == '__main__':
    array1 = [1, -2, 3, -1, 4]
    print(oneDimensionMaximumSubarry(array1))# 6
    array2 = [[2, 3, -1, 4],[1, -1, 0, -2], [4, -2, 3, 1]]
    print(twoDimensionMaximumSubarray(array2)) #12