import math

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

class RMQ:
    '''
    实现range maximum/minimum query区间最值查询
    空间复杂度nlog(n)
    时间复杂度nlog(n)
    table[i][j]表示从array[i]开始，连续2^j个元素构成的子数组中的最值
    '''
    def build(self, array, max = True):
        self.max = max
        log = int(math.log(len(array), 2)) + 1
        if max:
            self.table = [[-math.inf] * log for i in range(len(array))]
        else:
            self.table = [[math.inf] * log for i in range(len(array))]
        #初始化table[i][0] = array[i]
        for i in range(len(array)):
            self.table[i][0] = array[i]
        # DP：最优子表达式: table[i][j] = max(table[i][j-1], table[i + 2^(j-1)][j-1])
        # 这里要注意内外层循环
        # 及i取值范围: 因为要算的是从i开始的2^j个元素, 所以i应小于len(table)-2^j + 1
        for j in range(1, len(self.table[0])):
            for i in range(len(self.table) - int(math.pow(2, j)) + 1):
                self.table[i][j] = self.mm(self.table[i][j - 1], self.table[i + int(math.pow(2, j - 1))][ j - 1])

    def mm(self, a, b):
        '''
        根据self.max来决定是取最大还是取最小
        :param a:
        :param b:
        :return:
        '''
        if self.max:
            return max(a, b)
        else:
            return min(a, b)

    def getMM(self, i, j):
        k = int(math.log(j - i + 1, 2))
        return self.mm(self.table[i][k], self.table[j - int(math.pow(2, k)) + 1][k])

def lcs(root, n1, n2):
    node_array = []
    depth_array = []
    #DFS遍历，记录经过的每个点及其深度
    dfs(root, node_array, depth_array, 0)
    # 获取n1和n2在node_array中的地址
    i1 = node_array.index(n1.value)
    i2 = node_array.index(n2.value)
    # 保证i1 < i2
    if i1 > i2:
        i1, i2 = i2, i1
    rmq = RMQ()
    rmq.build(depth_array, max = False)
    ancestor_depth = rmq.getMM(i1, i2)
    ancestor_index = depth_array.index(ancestor_depth, i1, i2)
    # need fix 如果n1 是n2的ancestor
    return node_array[ancestor_index]

def dfs(root, node_array, depth_array, depth):
    node_array.append(root.value)
    depth_array.append(depth)
    if root.left is not None:
        dfs(root.left, node_array, depth_array, depth + 1)
        node_array.append(root.value)
        depth_array.append(depth)
    if root.right is not None:
        dfs(root.right, node_array, depth_array, depth + 1)
        node_array.append(root.value)
        depth_array.append(depth)

if __name__ == '__main__':
    # rmq = RMQ()
    # rmq.build([1, 2, 3, 4, 5])
    # print(rmq.table)
    # print(rmq.getMM(0, 4))
    # print(rmq.getMM(0, 0))
    # print(rmq.getMM(0, 1))
    # print(rmq.getMM(0, 2))
    # print(rmq.getMM(0, 3))
    n1 = Node(5)
    n2 = Node(3)
    n3 = Node(7)
    n4 = Node(2)
    n5 = Node(4)
    n6 = Node(6)
    n7 = Node(8)
    n8 = Node(1)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    res = lcs(n1, n8, n5)
    print(res)