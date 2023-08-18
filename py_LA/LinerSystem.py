from .Matrix import Matrix
from .Vector import Vector
from ._global import ZERO


class LinerSystem:
    def __init__(self, A, b):
        """
        A: 系数矩阵
        b: 结果向量
        """
        assert A.row_num() == len(b), "row number of A must be equal to the length of b"

        self._m = A.row_num()
        self._n = A.col_num()

        if isinstance(b, Vector):
            """
                    下面是实现增广矩阵的代码
                        增广矩阵就是 系数矩阵+结果列向量
                        使用向量类的underlying_list方法返回该向量的原数据（数据类型是列表）
                        再直接使用➕来链接结果列向量
                        这样实现一行的增广矩阵
                        再通过遍历来获得完整的增广矩阵
                    """
            self.Ab = [Vector(
                A.row_vector(i).underlying_list() + [b[i]]
            ) for i in range(self._m)]

        if isinstance(b, Matrix):
            """
            如果是矩阵，就在每一行加上该矩阵的某行
            """
            self.Ab = [Vector(
                A.row_vector(i).underlying_list() + b.row_vector(i).underlying_list()
            ) for i in range(self._m)]

        self.pivots = []

    def _max_row(self, index_i, index_j, n):
        """
        从第i行到第n行
        """
        best, ret = self.Ab[index_i][index_j], index_i
        """
        这里的self.Ab[i][index]就是取固定这一列，i进行行的递增变化
        为什么不直接使用[i][0]呢？
        因为不仅仅是第一次（第一行）需要选择最大行，往后确定每一行的主元的时候都要确定
        """
        for i in range(index_i + 1, n):
            if self.Ab[i][index_j] > best:
                # 此时，i是最大元素所在的行下标
                best, ret = self.Ab[i][index_j], i
        return ret

    def _forward(self):
        i, k = 0, 0

        while i < self._m and k < self._n:
            """
            为了避免[0][0]元素是零，所以直接选择第一列元素最大的这一行，和第一行交换
            看Ab[i][k]是否可以是主元
            """
            max_row = self._max_row(i, k, self._m)
            # 交换
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]
            if self.Ab[i][k] < ZERO:
                # 当这一个主元为0时，就在这一行的下一列找
                k += 1
            else:
                # 将这一行的主元化为1，就是这一行除以主元的值
                self.Ab[i] = self.Ab[i] / self.Ab[i][k]
                # 至此已经确定主元，现在将主元所在行以下的所有行的主元所在列的元素化为0
                for j in range(i + 1, self._m):
                    self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][k]
                self.pivots.append(k)
                i += 1

    def _backward(self):
        n = len(self.pivots)
        for i in range(n - 1, -1, -1):
            k = self.pivots[i]
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][k]

    def gauss_jordan_elimination(self):
        """
        如果有解，返回true，如果无解返回false
        """
        self._forward()
        self._backward()
        """
        self.pivots中记录的是所有主元的列下标，len(self.pivots)就是所有非零行的数量
        从len(self.pivots)到self._m都是为零的行
        因为增广矩阵的行最简形式，为零行都在下面
        现在只要判断为零行的最后一个元素是不是零，如果不是零，就无解
        """
        for i in range(len(self.pivots), self._m):
            if not self.Ab[i][-1] < ZERO:
                return False
            else:
                return True

    def fancy_print(self):
        """
        打印结果矩阵
        """
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|{}".format(self.Ab[i][-1]))


def inv(A):
    """
        求矩阵A的逆
        1. 如果不是方阵，就没有逆
        2. 创建一个线性系统，传入系数矩阵和n*n单位矩阵
        3. 调用高斯约旦消元法，得到行最简形式
        4. 如果有结果，最右边的就是所求的A的逆矩阵
    """
    if A.col_num() != A.row_num():
        return None

    n = A.row_num()
    # 下方传入了一个n*n的单位矩阵
    ls = LinerSystem(A, Matrix.identity(n))
    print(ls.gauss_jordan_elimination())
    if not ls.gauss_jordan_elimination():
        return None

    """
    从ls这个对象中取出Ab这个元素
    Ab从第0到第n-1列是行最简形式
        第n到第2n列是逆矩阵（因为单位矩阵列和系数矩阵行相同）
    """
    invA = [[row[i] for i in range(n, n * 2)] for row in ls.Ab]
    return Matrix(invA)
