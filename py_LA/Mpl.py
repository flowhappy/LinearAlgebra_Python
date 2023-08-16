from py_LA.Matrix import Matrix
import math


# 矩阵变换库
class MplMtr:
    """
        矩阵变换类
        使用这个类创建的矩阵，自带变换方法
    """

    def __init__(self, lst2d):
        self._values = Matrix(lst2d).T()

    def __repr__(self):
        return "Mpl{}".format(self._values)

    __str__ = __repr__

    @staticmethod
    def get_points(mtr):
        return [mtr.col_vector(i)[0] for i in range(mtr.col_num())], \
            [mtr.col_vector(i)[1] for i in range(mtr.col_num())]

    def transform_mtr(self, lst2d):
        """
        根据传入的变换矩阵，返回变化后的矩阵
        """
        return self.get_points(Matrix(lst2d).dot_mul(self._values))

    def x_axis_flip(self):
        # 沿X轴翻转 的变换矩阵
        return self.transform_mtr([[1, 0], [0, -1]])

    def y_axis_flip(self):
        # 沿Y轴翻转 的变换矩阵
        return self.transform_mtr([[-1, 0], [0, 1]])

    def o_flip(self):
        # 关于原点对称 的变换矩阵
        return self.transform_mtr([[-1, 0], [0, -1]])

    def x_shear(self, k):
        # 沿X轴错切 的变换矩阵
        return self.transform_mtr([[1, k], [0, 1]])

    def y_shear(self, k):
        # 沿Y轴错切 的变换矩阵
        return self.transform_mtr([[1, 0], [k, 1]])

    def rotate(self, theta):
        # 旋转
        return self.transform_mtr([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])
