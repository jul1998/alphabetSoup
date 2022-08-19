import random
def open_words_txt():
    # Extract words from txt file
    with open("words.txt", "r") as f:
        return f.read().splitlines()


class Directions:

    def __init__(self, matrix, occupied):
        self.occupied = occupied  # Gets boolean_matrix created in main file
        self.matrix = matrix  # Gets matrix created in main file
        self.rows = len(matrix)  # Access to matrix rows
        self.columns = len(matrix[0])  # Access to first list in self.rows

    def check_if_available_columns(self, occupied, word_length, row, column):
        for letter in range(word_length):  # For columns, check for every letter in word
            # if spaces are not occupied (False) to overwrite them in matrix
            if occupied[row][column]:
                return True
            elif column >= word_length:
                return True
        return False

    def check_if_available_rows(self,occupied, row, column, word_lenght):  # For rows, check for every letter in word
            # if spaces are not occupied (False) to overwrite them in matrix
            for row in range(word_lenght):
                if occupied[row][column]:
                    return True
                elif row >= word_lenght:
                    return True
            return False

    def left_to_right(self, matrix, occupied, word):  # Overwrite words from left to right in matrix
        random_index = random.randint(0, self.columns - 2)  # Generates random number to place words randomly in matrix

        def write_left_to_right(matrix, row, column, word):  # Gets index and letter to overwrite spaces in matrix
            # accordingly
            for index, letter in enumerate(word):
                matrix[row][column + index] = letter
            return matrix

        for row in range(self.rows):
            for column in range(self.columns):
                if not self.check_if_available_columns(occupied, len(word), row+random_index, column):  # Whenever
                    # check_if_available_columns is False, then it can continue
                    matrix = write_left_to_right(matrix, row+random_index, column, word)
                    occupied = write_left_to_right(occupied, row+random_index, column, [True] * len(word))
                    return True, matrix, occupied  # If successful, return True with matrix and boolean_matrix modified
        return False, matrix, occupied  # If not successful, return True with matrix and boolean_matrix modified

    def right_to_left(self, matrix, occupied, word): # Overwrite words from right to left in matrix
        random_index = random.randint(0, self.columns - 2) # Generates random number to place words randomly in matrix

        def write_right_to_left(matrix, row, column, word): # Gets index and letter to overwrite spaces in matrix
            # accordingly
            for index, letter in enumerate(word):
                matrix[row][column + index] = letter
            return matrix

        reversed_word = word[::-1]
        for row in range(self.rows):
            for column in range(self.columns):
                if not self.check_if_available_columns(occupied, len(reversed_word), row + random_index, column):  # Whenever
                    # check_if_available_columns is False, then it can continue
                    matrix = write_right_to_left(matrix, row + random_index, column, reversed_word)
                    occupied = write_right_to_left(occupied, row + random_index, column, [True] * len(word))
                    return True, matrix, occupied # If successful, return True with matrix and boolean_matrix modified
        return False, matrix, occupied # If not successful, return True with matrix and boolean_matrix modified

    def top_to_bottom(self, matrix, occupied, word): # Overwrite words from top to bottom in matrix
        random_index = random.randint(0, self.rows - 2) # Generates random number to place words randomly in matrix

        def overwrite_top_to_bottom(matrix, word, row, column):  # Gets index and letter to overwrite spaces in matrix
            for index, letter in enumerate(word):
                matrix[row + index][column] = letter
            return matrix

        for row in range(self.rows):
            for column in range(self.columns):
                if not self.check_if_available_rows(occupied, row, column + random_index, len(word)): # Whenever
                    # check_if_available_columns is False, then it can continue
                    matrix = overwrite_top_to_bottom(matrix, word, row, column + random_index)
                    occupied = overwrite_top_to_bottom(occupied, [True] * len(word), row, column + random_index)
                    return True, matrix, occupied  # If successful, return True with matrix and boolean_matrix modified
        return False, matrix, occupied  # If not successful, return True with matrix and boolean_matrix modified


    def bottom_to_top(self, matrix, occupied, word): # Overwrite words from top to bottom in matrix
        reversed_word = word[::-1]
        random_index = random.randint(0, self.rows - 2)  # Generates random number to place words randomly in matrix

        def overwrite_bottom_to_top(matrix, row, column, word): # Gets index and letter to overwrite spaces in matrix
            for index, letter in enumerate(word):
                matrix[row+index][column] = letter
            return matrix

        for row in range(self.rows):
            for column in range(self.columns):
                if not self.check_if_available_rows(occupied, len(reversed_word), row + random_index, column): # Whenever
                    # check_if_available_columns is False, then it can continue
                    matrix = overwrite_bottom_to_top(matrix, row + random_index, column, reversed_word)
                    occupied = overwrite_bottom_to_top(occupied, row + random_index, column, [True] * len(reversed_word))
                    return True, matrix, occupied # If successful, return True with matrix and boolean_matrix modified
        return False, matrix, occupied

    def diagonal(self, matrix, occupied, word):
        def check_if_available(occupied, word_length, row, column):
            for index, letter in enumerate(word_length):
                if occupied[row+index][column+index]:
                    return True
                elif column >= len(word_length):
                    return True
            return False

        def overwrite_diagonal(matrix, word, row, column):
            for index, letter in enumerate(word):
                matrix[row+index][column+index] = letter
            return matrix

        for row in range(self.rows):
            for column in range(self.columns):
                if not check_if_available(occupied, word, row, column):
                    matrix = overwrite_diagonal(matrix, word, row, column)
                    occupied = overwrite_diagonal(occupied, [True] * len(word), row, column)
                    return True, matrix, occupied
        return False, matrix, occupied