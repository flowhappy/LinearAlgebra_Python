class Determinant:

    def __init__(self, matrix):
        self._values = matrix
        self._row_num = len(matrix)
        self._flag = 1

    def same_row(self):
        """
        判断有没有相同的行
        :return: 返回相同行数的数量
        这里如果使用常规的双重循环效率更高，因为计算到第二个就可以返回了，但是这个写法比较酷
        """
        return sum(
            [self._values[i] == self._values[j] for i in range(self._row_num - 1) for j in range(i + 1, self._row_num)]
        )

    def max_row(self, index):
        """
        选择最大元素行下标
        :param index: 当前要比较的行
        :return: 最大元素行下标
        """
        max_index = index
        max_e = self._values[max_index][index]
        for i in range(index + 1, self._row_num):
            if abs(self._values[i][index]) > max_e:
                max_index, max_e = i, self._values[max_index][index]
                # 发生一次交换，行列式×-1，这里直接取一个符号，最后和结果相乘
                self._flag = self._flag * -1
        return max_index

    def triangle_up(self):
        """
        返回上三角矩阵
        为了避免除零的情况，依旧像高斯消元要交换最大行
        """
        for i in range(self._row_num - 1):
            max_index = self.max_row(i)
            self._values[i], self._values[max_index] = self._values[max_index], self._values[i]
            for j in range(i + 1, self._row_num):
                k = self._values[j][i] / self._values[i][i]
                for l in range(self._row_num):
                    self._values[j][l] = self._values[j][l] - self._values[i][l] * k

    def result(self):
        """
        :return: 有相同行直接返回0，否则计算主对角线乘积
        """
        if not self.same_row():
            res = 1
            self.triangle_up()
            for i in range(self._row_num):
                res = res * self._values[i][i]
            return res * self._flag
        else:
            return 0
