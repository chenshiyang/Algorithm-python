def lcs(s1, s2):
    '''
    DP实现最长公共子序列

    :param s1:
    :param s2:
    :return:
    '''
    if s1 is None or s2 is None or len(s1) == 0 or len(s2) == 0:
        return 0
    carry = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                carry[i][j] = carry[i - 1][j - 1] + 1
            else:
                carry[i][j] = max(carry[i][j - 1], carry[i - 1][j])

    #查表回溯输出一个最长公共子序列
    cs = []
    i = len(s1)
    j = len(s2)
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            cs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif carry[i - 1][j] > carry[i][j - 1]:
            i -= 1
        else:
            j -= 1
    cs.reverse()
    print(cs)

    return carry[len(s1)][len(s2)]

if __name__ == '__main__':
    s1 = '13456778'
    s2 = '357486782'
    print(lcs(s1, s2))