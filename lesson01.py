class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        for row in self.list:
            for i in row:
                print(f"{i}", end=" ")
            print()
        return ''

    def __add__(self, other):
        for row in range(len(self.list)):
            for i in range(len(self.list[row])):
                self.list[row][i] = self.list[row][i] + other.list[row][i]
        return Matrix.__str__(self)


m1 = Matrix([[1, 2, 3], [1, 4, 8], [1, 5, 8], [1, 5, 77]])
m2 = Matrix([[0, 9, 9], [8, 5, 0], [4, 2, 4], [2, 4, 7]])
print(m1.__add__(m2))
