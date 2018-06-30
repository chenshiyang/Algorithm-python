def longestCommonSubsequence(s1, s2):
    '''
    返回s1和s2的最长公共子序列的长度
    :param s1:
    :param s2:
    :return:
    '''
    if s1 is None or s2 is None or len(s1) == 0 or len(s2) == 0:
        return 0
    m = len(s1) + 1
    n = len(s2) + 1
    # 生成m x n的二维数组
    table = [[0] * n for i in range(m)]
    maxLength = 0
    for i in range(1, m):
        for j in range(1, n):
            # 因为table下标是从1开始的, s1 s2下标是从0开始的, 所以这里要这一下标的转换
            table[i][j] = table[i - 1][j - 1] + 1 if s1[i - 1] == s2[j - 1] else max(table[i - 1][j], table[i][j - 1])
            maxLength = max(maxLength, table[i][j])
    return maxLength

if __name__ == '__main__':

    s1 = 'abcde'
    s2 = 'bace'
    print(s1, s2, longestCommonSubsequence(s1, s2))
    s3 = None
    s4 = 'abc'
    print(s3, s4, longestCommonSubsequence(s3, s4))
    s5 = ''
    s6 = 'abc'
    print(s5, s6, longestCommonSubsequence(s5, s6))
    s7 = 'a'
    s8 = 'abc'
    print(s7, s8, longestCommonSubsequence(s7, s8))