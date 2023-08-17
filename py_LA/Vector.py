import math
from ._global import ZERO


class Vector:
    """
    向量类

    除了常见的二维向量（2，3），三位向量（2，3，4）
    我们还可以将一些信息用向量的描述方法保存
        学号：2，性别：1，身高：180，年龄：22，身份：9，权限：10
        可以描述为：（2，1，180，22，9，10），这是抽象向量
    """

    def __init__(self, lst):
        """
        构造方法，用户通过该方法传入参数实例化对象
        :param lst: 传入的参数是列表（贴切的模拟向量的数据存储方式）
        """
        # 为了安全使用复制后的参数
        self._values = list(lst)

    def __repr__(self):
        """
        是系统调用的魔术方法，将鼠标悬停在实例化后的对象上，将会显示该对象的信息
        如：vec: Vector = Vector([2, 5])
        """
        return f'Vector({self._values})'

    def __str__(self):
        """
        用户打印出的结果
        :return: {}里的内容是format的内容，
                将列表遍历时的每个元素强转成str类型，再用逗号链接
                最后输出的效果就是我们常见的向量的表示方法
                如：（2，5）
        """
        return "({})".format(", ".join(str(i) for i in self._values))

    def __len__(self):
        """
        :return: 重载方法，返回向量的长度
        """
        return len(self._values)

    def __getitem__(self, index):
        """
        通过用户输入的下标，获取向量中对应的元素
        :param index: 用户输入的下标
        :return: 返回的对应的元素
        """
        return self._values[index]

    def __iter__(self):
        return self._values.__iter__()

    def __add__(self, other):
        """

        :param other: 另一个Vector对象
        :return:
            1. 返回对象是新的一个Vector类，该类的构造函数要传入一个列表，所以是 Vector([])
            2. zip()函数参考笔记，注意：zip()中的是可迭代对象
            3. zip()中原来的写法是：self._values,other._values,但因为安全考虑，不能这样写
               我们给这个类添加一个迭代器 __iter__,这样新建的对象是可迭代的
               迭代器返回 self._values.__iter__
               注意：self._values是列表，它是有迭代器的，所以返回它的迭代器
            4. 现在，因为给Vector添加了__iter__方法，所以zip(self,other)的写法并不会报错
               他们现在是可迭代对象，当zip()调用这两个对象的迭代器时，就会调用到self._values.__iter__
        """
        # 使用断言来判断两个向量的长度（种类）是不是一种，如果不是，就结束程序并触发异常
        assert len(self) == len(other), "not the same length vector"
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        assert len(self) == len(other), "not the same length vector"
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, k):
        return Vector([e * k for e in self._values])

    def __rmul__(self, k):
        """
        :return: 这里直接使用*，是因为上面已经定义了__mul__这个方法，可以使用*了
        """
        return self * k

    def __truediv__(self, k):
        # 定义浮点数除法
        # 计算机数学的除法中，0是不能直接和变量去比的，考虑丢精问题
        if self.norm() < ZERO:
            raise ZeroDivisionError("Norm is zero")
        return 1 / k * self

    def __pos__(self):
        # 正向量
        return self * 1

    def __neg__(self):
        # 负向量
        return -1 * self

    # 类方法 详情见笔记
    @classmethod
    def zero(cls, dim):
        """
        :param dim: 向量的纬度
        :return: dim纬度的零向量
        """
        return cls([0] * dim)

    def norm(self):
        """
        :return: 返回向量的模
        """
        return math.sqrt(sum(math.pow(e, 2) for e in self))

    def normalize(self):
        return self / self.norm()

    def dot_mul(self, other):
        # 点乘： x1x2+y1y2
        assert len(self) == len(other), "not the same length vector"
        return sum(a * b for a, b in zip(self, other))

    def underlying_list(self):
        """
        返回底层列表
        """
        return self._values
