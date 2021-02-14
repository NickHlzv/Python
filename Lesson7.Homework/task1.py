class Matrix:
    def __init__(self, list_of_lists: list):
        self.base_dimension = 0
        self.len_dimension = len(list_of_lists)
        self.list_of_lists = list_of_lists
        for list in self.list_of_lists:
            self.base_dimension = len(list) if len(list) > self.base_dimension else self.base_dimension
        for list in self.list_of_lists:
            while len(list) < self.base_dimension:
                list.append(0)

    def __str__(self):
        result = ''
        for lst in self.list_of_lists:
            string = str(lst)
            result += (string + '\n')
        return result

    def __add__(self, matrix):
        sum_base_dimension = matrix.base_dimension if matrix.base_dimension > self.base_dimension else self.base_dimension
        sum_len_dimension = matrix.len_dimension if matrix.len_dimension > self.len_dimension else self.len_dimension
        result = []
        for i in range(sum_len_dimension):
            if i < len(self.list_of_lists):
                self_string = self.list_of_lists[i].copy()
                while len(self_string) < sum_base_dimension:
                    self_string.append(0)
            if i < len(matrix.list_of_lists):
                matrix_string = matrix.list_of_lists[i].copy()
                while len(matrix_string) < sum_base_dimension:
                    matrix_string.append(0)
            if i >= len(self.list_of_lists):
                self_string = [0 for i in range(sum_base_dimension)]
            if i >= len(matrix.list_of_lists):
                matrix_string = [0 for i in range(sum_base_dimension)]
            new_string = [self_string[ind] + matrix_string[ind] for ind in range(sum_base_dimension)]
            result.append(new_string)
        return result


matrix1 = Matrix([[1, 5, 6], [4, 2, 15], [5, 7, 1, 1]])
print(matrix1)
matrix2 = Matrix([[2], [0, 5, 6, 6, 7], [3, 0, 1], [2, 4, 8]])
print(matrix2)
matrix3 = Matrix(matrix1 + matrix2)
print(matrix3)
print(matrix1)
print(matrix2)
print(Matrix(matrix1 + matrix3))
