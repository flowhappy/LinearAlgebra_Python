from py_LA.Vector import Vector

if __name__ == '__main__':
    vec = Vector([2, 5])

    print(vec)
    print(type(vec))
    print(vec.__len__())

    print(vec.__getitem__(1))

    vec2 = Vector([3, 4])

    print("{} + {} = {}".format(vec, vec2, vec + vec2))

    print("{} - {} = {}".format(vec, vec2, vec - vec2))

    print("{} * 3 = {}".format(vec, vec * 3))
    print("3 * {} = {}".format(vec, 3 * vec))

    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    zero_vec = Vector.zero(3)
    print(zero_vec)

    print(vec.norm())

    print(vec.normalize().norm())

    print(vec.dot_mul(vec2))
