from py_LA.Determinant import Determinant

# det1 = Determinant([[1, 4, -1, 4], [2, 2, 2, 3], [3, -1, 6, 2], [4, 0, 5, 3]])
# det2 = Determinant([[0, 5, 2, 0], [8, 3, 5, 4], [7, 2, 4, 1], [0, 4, 1, 0]])
# det3 = Determinant([[2, 2, 2], [2, 2, 2], [3, 3, 3]])

lst = list()
dim = int(input('please input the dimension you wanna calculate: '))
for i in range(dim):
    lst_inner = list()
    print('please input {} row\'s element:'.format(i+1))
    for j in range(dim):
        try:
            lst_inner.append(int(input()))
        except ValueError:
            print('input one number a time and press the <enter> key\n'
                  f'please re-input the number for row{i+1} one by one with <enter> key:')
            lst_inner.append(int(input()))

    lst.append(lst_inner)
print(f'the determinant is {lst}')

print(f'the result of this determinant is {Determinant(lst).result()}')
