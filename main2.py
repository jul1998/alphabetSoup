import random
rows = 10
columns = 10

abc = "abcdefhijklmnopqrsuvwxyz"

word_list = ["BLUE", "RED", "BLACK", "WHITE","GREEN"]
random_word = random.choice(word_list)

def create_matrix():
    matrix = []
    bool_matrix = []
    for row in range(rows):
        matrix.append([]), bool_matrix.append([])
        for col in range(columns):
            random_abc = random.choice(abc)
            matrix[row].append("*"), bool_matrix[row].append(False)
    return matrix, bool_matrix



def fix_matrix(matrix):
    fixed_matrix = ""
    for row in matrix:
        for letter in row:
            fixed_matrix += str(letter) + "|"
        fixed_matrix += "\n"
    return fixed_matrix

def is_left_to_right(bool_matrix,word,row,col):
    for _ in word:
        if bool_matrix[row][col]:
            return False
    return True


def left_to_right(bool_matrix,matrix, word):
    random_index = random.randint(0,len(matrix)-1)

    def overwrite_left_to_right(matrix, row,col, word):
        for index, letter in enumerate(word):
            matrix[row][col+index] = letter
        return matrix
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if is_left_to_right(bool_matrix,word,row + random_index,col):
                matrix = overwrite_left_to_right(matrix,row + random_index,col,word)
                bool_matrix = overwrite_left_to_right(bool_matrix,row + random_index,col, [True]*len(word))
                return bool_matrix, matrix
    return bool_matrix, matrix

def is_top_to_bottom(bool_matrix,word,row,col):
    for index, _ in enumerate(word):
        if bool_matrix[row+index][col]:
            return False
    return True

def top_to_bottom(bool_matrix,matrix, word):
    random_index = random.randint(0, len(matrix) - 1)
    def overwrite_top_to_bottom(matrix, row, col, word):
        for index, letter in enumerate(word):
            matrix[row+index][col] = letter
        return matrix
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if is_top_to_bottom(bool_matrix,word,row,col + random_index):
                matrix = overwrite_top_to_bottom(matrix, row, col + random_index, word)
                bool_matrix = overwrite_top_to_bottom(bool_matrix, row, col + random_index, [True] * len(word))
                return bool_matrix, matrix
    return bool_matrix, matrix

def bottom_to_top(bool_matrix,matrix, word):
    random_index = random.randint(0, len(matrix) - 1)
    reversed_word = word[::-1]
    def overwrite_bottom_to_top(matrix, row, col, reversed_word):
        for index, letter in enumerate(reversed_word):
            matrix[row+index][col] = letter
        return matrix
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if is_top_to_bottom(bool_matrix,reversed_word,row,col + random_index):
                matrix = overwrite_bottom_to_top(matrix, row, col + random_index, reversed_word)
                bool_matrix = overwrite_bottom_to_top(bool_matrix, row, col + random_index, [True] * len(reversed_word))
                return bool_matrix, matrix
    return bool_matrix, matrix


def main():
    matrix, bool_matrix = create_matrix()
    directions = [top_to_bottom, left_to_right, bottom_to_top]
    for word in word_list:
        try:
            random_direction = random.choice(directions)
            bool_matrix, matrix = random_direction(bool_matrix, matrix, word)
        except IndexError:
            print(f"Word {word} did not fit properly")
            random_direction = random.choice(directions)
            bool_matrix, matrix = random_direction(bool_matrix, matrix, word)
        else:
            pass
    print(fix_matrix(matrix))


if __name__ == '__main__':
    main()

