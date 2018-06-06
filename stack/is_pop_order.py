from collections import deque

def isPopOrder(array, barry):
    '''
    第一个序列是压栈顺序,判断第二个序列是不是一种可能的出栈顺序

    :param array:
    :param barry:
    :return:
    '''
    if array is None or barry is None or len(array) != len(barry):
        return False
    stack = deque()

    i = 0
    j = 0
    while i < len(array) or j < len(barry):
        if len(stack) > 0 and stack[0] == barry[j]:
            stack.popleft()
            j += 1
            continue
        elif i == len(array):
            return False
        else:
            stack.appendleft(array[i])
            i += 1
    return len(stack) == 0

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    barry = [4, 5, 3, 2, 1]
    carry = [4, 3, 5, 1, 2]
    darry = [1, 2, 5, 4, 3]
    print(isPopOrder(array, barry))
    print(isPopOrder(array, carry))
    print(isPopOrder(array, darry))