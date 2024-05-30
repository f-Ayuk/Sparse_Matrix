import os

class SparseMatrix:

    def __init__(self, matrixFilePath):
        self.matrix = self.read_sparse_matrix(matrixFilePath)

    def read_sparse_matrix(self, matrixFilePath):
        matrix = {}
        with open(matrixFilePath, 'r') as file:
            lines = file.readlines()
            rows = int(lines[0].split('=')[1].strip())
            cols = int(lines[1].split('=')[1].strip())
            for line in lines[2:]:
                line = line.replace('(', '').replace(')', '').split(',')
                row = int(line[0])
                col = int(line[1])
                value = int(line[2])
                matrix[(row, col)] = value
        return matrix

    def getElement(self, currRow, currCol):
        return self.matrix.get((currRow, currCol), 0)

    def setElement(self, currRow, currCol, value):
        self.matrix[(currRow, currCol)] = value

    def addition(self, other_matrix):
        result = {}
        for (row, col), value in self.matrix.items():
            result[(row, col)] = value + other_matrix.get((row, col), 0)
        for (row, col), value in other_matrix.items():
            if (row, col) not in self.matrix:
                result[(row, col)] = value
        return result

    def subtraction(self, other_matrix):
        result = {}
        for (row, col), value in self.matrix.items():
            result[(row, col)] = value - other_matrix.get((row, col), 0)
        for (row, col), value in other_matrix.items():
            if (row, col) not in self.matrix:
                result[(row, col)] = -value
        return result

    def multiplication(self, other_matrix):
        result = {}
        for (row1, col1), val1 in self.matrix.items():
            for (row2, col2), val2 in other_matrix.items():
                if col1 == row2:
                    result[(row1, col2)] = result.get(
                        (row1, col2), 0) + val1 * val2
        return result







class SparseMatrix:
    def __init__(self, sample_input_for_students):
        self.matrix = self.read_sparse_matrix(sample_input_for_students)
        self.matrix_files = [f for f in os.listdir(sample_input_for_students) if f.endswith('.txt')]
        self.matrices = {matrix_file: self.read_sparse_matrix(os.path.join(sample_input_for_students, matrix_file)) for matrix_file in self.matrix_files}

    def read_sparse_matrix(self, sample_input_for_students):
        matrix = {}
        with open(sample_input_for_students, 'r') as file:
            lines = file.readlines()
            rows = int(lines[0].split('=')[1].strip())
            cols = int(lines[1].split('=')[1].strip())
            for line in lines[2:]:
                line = line.replace('(', '').replace(')', '').split(',')
                row = int(line[0])
                col = int(line[1])
                value = int(line[2])
                matrix[(row, col)] = value
        return matrix

    def getElement(self, currRow, currCol):
        return self.matrix.get((currRow, currCol), 0)

    def setElement(self, currRow, currCol, value):
        self.matrix[(currRow, currCol)] = value

    def addition(self, other_matrix):
        result = {}
        for (row, col), value in self.matrix.items():
            result[(row, col)] = value + other_matrix.get((row, col), 0)
        for (row, col), value in other_matrix.items():
            if (row, col) not in self.matrix:
                result[(row, col)] = value
        return result

    def subtraction(self, other_matrix):
        result = {}
        for (row, col), value in self.matrix.items():
            result[(row, col)] = value - other_matrix.get((row, col), 0)
        for (row, col), value in other_matrix.items():
            if (row, col) not in self.matrix:
                result[(row, col)] = -value
        return result

    def multiplication(self, other_matrix):
        result = {}
        for (row1, col1), val1 in self.matrix.items():
            for (row2, col2), val2 in other_matrix.items():
                if col1 == row2:
                    result[(row1, col2)] = result.get((row1, col2), 0) + val1 * val2
        return result