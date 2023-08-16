import math
from py_LA.Mpl import MplMtr
import matplotlib.pyplot as plt
#
if __name__ == '__main__':

    points = [
        [0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
        [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]
    ]
    x = [points[i][0] for i in range(len(points))]
    y = [points[i][1] for i in range(len(points))]
    # 调整绘制窗口的大小
    plt.figure(figsize=(5, 5))
    # X轴从-10到10
    plt.xlim(-10, 10)
    # Y轴从-10到10
    plt.ylim(-10, 10)
    plt.plot(x, y)

    """
    和作业相关
    """
    mpl = MplMtr(points)
    x, y = mpl.rotate(math.pi / 3)
    plt.plot(x, y)

    plt.show()
