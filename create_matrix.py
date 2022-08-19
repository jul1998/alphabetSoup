import random

abc = "abcdefhijklmnopqrsuvwxyz"


class CreateMatrix:

    def __init__(self):
        self.matrix = []
        self.boolean_matrix = []

    def create_matrix(self, rows, columns):
        # Matrix is where random characters will be placed and what users will see
        # Boolean_matrix is to identify where
        # words from txt can take place depending on if place is available (True) or not (False)

        for row in range(rows):  # Iterating in matrix rows
            self.matrix.append([]), self.boolean_matrix.append(
                [])  # Here we are appending a new empty list to matrix and boolean_matrix
            for colum in range(columns):  # Iterating in matrix and boolean matrix columns
                char = abc[random.randint(0, len(abc) - 1)]  # Generate random characters for matrix columns
                self.matrix[row].append("*")  # Access to row number where a random character will be placed in each
                # column. "*" should be replaced by var char if wanted to user char
                self.boolean_matrix[row].append(
                    False)  # Access to row number where a False value  will be placed in each column
        return self.matrix, self.boolean_matrix

    def fix_matrix(self, matrix):
        rows = len(self.matrix)  # Access to rows in matrix
        columns = len(self.matrix[0])  # Access to columns in matrix
        fixed_matrix = " "  # Empty string to store characters in matrix
        for row in range(rows):
            for colum in range(columns):
                fixed_matrix += matrix[row][
                                    colum] + "|"  # Access to each row in matrix, then access to each column where a
                # character(string) is located
            fixed_matrix += "\n"  # Once it iterated over all columns, add an enter and go for the next row
        return fixed_matrix
