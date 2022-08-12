import random


# Aqui se carga el txt con las palabras
def words():
    with open("sopa.txt", "r") as f:
        return f.read().splitlines()


abc = "abcdefhijklmnopqrsuvwxyz"


def create_matrix(n_rows, n_columns):
    m, bool_m = [], []
    for r in range(n_rows):
        m.append([]), bool_m.append([])
        for c in range(n_columns):
            char = abc[random.randint(0, len(abc) - 1)]
            m[r].append(char), bool_m[r].append(False)

    return m, bool_m


def de_izquierda_a_derecha(matrix, word, occupied):
    rows = len(matrix)
    col = len(matrix[0])
    ram = random.randint(0, rows - 1)
    for r in range(rows):
        for c in range(col):
            if not any(occupied[r + ram][c:len(word)]):
                matrix[r + ram][c:len(word)] = word
                occupied[r + ram][c:len(word)] = [True] * len(word)
            return True, matrix, occupied
    return False, matrix, occupied


def escribir_derecha_a_izquierda(matrix, word, r, c):
    """Funcion que permite sobreescribir letras en matriz"""
    for index, letter in enumerate(word):
        matrix[r][c + index] = letter
    return matrix


def derecha_a_izquierda(matrix, word, occupied):
    reversed_word = word[::-1]
    rows = len(matrix)
    col = len(matrix[0])
    ram = random.randint(0, rows - 1)
    for r in range(rows):
        for c in range(col):
            # if not verificar_derecha_a_izquierda(occupied, len(word), r, c):
            if not any(occupied[r + ram][c:len(word)]):
                matrix = escribir_derecha_a_izquierda(matrix, reversed_word, r + ram, c)
                occupied = escribir_derecha_a_izquierda(occupied, [True] * len(reversed_word), r + ram, c)
            return True, matrix, occupied
    return False, matrix, occupied


def escribir_arriba_a_abajo(matrix, word, r, c):
    """Funcion que permite sobreescribir letras de arriba a abajo en matriz"""
    for index, letter in enumerate(word):
        matrix[r + index][c] = letter
    return matrix


def arriba_a_abajo(matrix, word, occupied):
    def check_si_ocupado(occupied, word_lenght, r, c):
        """Funcion que permite verificar si hay espacios disponibles en la matriz de booleans"""
        for r in range(word_lenght):
            if occupied[r][c]:
                return True
        return False

    rows = len(matrix)
    col = len(matrix[0])
    ram = random.randint(0, col - 1)
    for r in range(rows):
        for c in range(col):
            if not check_si_ocupado(occupied, len(word), r, c + ram):  # Si hay espacios disponibles en la matriz de booleans
                matrix = escribir_arriba_a_abajo(matrix, word, r, c + ram)
                occupied = escribir_arriba_a_abajo(occupied, [True] * len(word), r, c + ram)
                return True, matrix, occupied
    return False, matrix, occupied


def abajo_a_arriba(matrix, word, occupied):
    def check_si_ocupado(occupied, word_lenght, r, c):
        for r in range(word_lenght):
            if occupied[r][c]:
                return True
        return False

    reversed_word = word[::-1]
    rows = len(matrix)
    col = len(matrix[0])
    ram = random.randint(0, col - 1)
    for r in range(rows):
        for c in range(col):
            if not check_si_ocupado(occupied, len(reversed_word), r, c + ram):
                matrix = escribir_arriba_a_abajo(matrix, reversed_word, r, c + ram)
                occupied = escribir_arriba_a_abajo(occupied, [True] * len(reversed_word), r, c + ram)
                return True, matrix, occupied
    return False, matrix, occupied


def escribir_diagonal(matrix, word, r, c):
    for index, letter in enumerate(word):
        matrix[r + index][c + index] = letter
    return matrix


def diagonal(matrix, word, occupied):
    def check_si_ocupado(occupied, word_lenght, r, c):
        for index, letter in enumerate(word_lenght):
            if occupied[r + index][c + index]:
                return True
        return False

    rows = len(matrix)
    col = len(matrix[0])
    for r in range(rows):
        for c in range(col):
            if not check_si_ocupado(occupied, word, r, c):  # Si hay espacios disponibles en la matriz de booleans
                matrix = escribir_diagonal(matrix, word, r, c)
                occupied = escribir_diagonal(occupied, [True] * len(word), r, c)
            return True, matrix, occupied
    return False, matrix, occupied


def fix_matrix(matrix):
    fix_matrix = " "
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            fix_matrix += str(matrix[r][c]) + "|"
        fix_matrix += "\n"
    return fix_matrix


def main():
    rows = 10
    col = 10
    matrix, bool_m = create_matrix(rows, col)
    directions = [derecha_a_izquierda, de_izquierda_a_derecha, arriba_a_abajo, abajo_a_arriba, diagonal]
    for word in words():
        direction = directions[random.randint(0, len(directions) - 1)]  # Se escoge una direccion de la lista directions
        success, matrix, bool_m = direction(matrix, word, bool_m)
        if not success:
            print(f"La palabra {word} no cupo")
            break
    print(fix_matrix(matrix))

    def registrar_palabra(matrix, bool_m):
        words_found = [] #Palabras encontradas correctamente por el usuario
        while len(words_found) != len(words()):
            should_continue = input("Desea continuar con el juego? 'Y' o 'N'").upper()
            if should_continue == "N":
                print("Juego terminado")
                break
            else:

                word_found_by_user = input("Ingrese la palabra encontrada: ").lower() #Supuesta palabra encontrada por usuario
                if word_found_by_user in words_found:
                    print(f"{word_found_by_user} ya fue encontrada. Escoja otra palabra")
                else:
                    # letter_found, row_position, col_position estan dentro del foor loop para renovar inputs por iteracion
                    letters_found_list = ""
                    while len(letters_found_list) < len(word_found_by_user):
                    #for i in range(len(word_found_by_user)):
                        letter_found = input("Introduzca la letra encontrada: ").lower()
                        row_position = int(input("Coloque el numero de la fila donde esta la letra: ")) - 1
                        col_position = int(input("Coloque el numero de la columna donde esta la letra: ")) - 1

                        m_rows = matrix[row_position]  # Accede a filas de matriz
                        m_char_in_column = m_rows[col_position]  # Accede a caracter en filas de matriz
                        bool_rows = bool_m[row_position]
                        bool_char_in_col = bool_rows[col_position]


                        if m_char_in_column == letter_found and bool_char_in_col == True:
                            print(f"La letra {letter_found} fue encontrada en la fila {row_position}, columna {col_position}")
                            matrix[row_position][col_position] = letter_found.upper()
                            letters_found_list += letter_found
                            print(fix_matrix(matrix))

                        else:
                            print(f"{letter_found} no pertenece a palabra {word_found_by_user} dentro de sopa de letras")
                    words_found.append(word_found_by_user) #Esto va a pasar unicamente si el usuario logra ingresar las letras correctamente
                    print(words_found)
        if len(words_found) == 0:
             print("Ninguna palabra fue encontrada")
        elif len(words_found) == len(words()):
            print("Todas las palabras fueron encontradas")
            for word in words_found:
                print(word)
        else:
            print("Palbras que fueron encontradas: ")
            for word in words_found:
                print(word)
    print(registrar_palabra(matrix, bool_m))


if __name__ == '__main__':
    main()











