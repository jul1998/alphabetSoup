from create_matrix import CreateMatrix
from directions import Directions, open_words_txt
import random




def main():
    rows = 12 #int(input("Enter number of rows "))
    columns = 12 #int(input("Enter number of columns "))
    create_matrix = CreateMatrix()  # Stores class CreateMatrix in variable


    matrix, boolean_matrix = create_matrix.create_matrix(rows,
                                                         columns)  # Stores both matrix and boolean_matrix in variables

    direction = Directions(matrix, occupied=boolean_matrix)
    directions_list = [direction.left_to_right,
                       direction.right_to_left,
                       direction.top_to_bottom,
                       direction.bottom_to_top,
                       direction.diagonal
                       ]

    for word in open_words_txt():
        random_direction = directions_list[random.randint(0, len(directions_list)-1)]
        success, matrix, boolean_matrix = random_direction(matrix, boolean_matrix, word)  # Success takes the
        # boolean value,matrix will take matrix outcome after placing the word ,
        # and boolean_matrix takes the occupied matrix outcome
        if not success:  # If word does not fit, then success will be false
            print(f"{word} did not fit")
    print(create_matrix.fix_matrix(matrix))  # This what the user will see as final outcome

    def play_Game():  # From here, the user will play the game
        words_found = []  # Empty list to store any word found by user
        while len(words_found) < len(open_words_txt()):
            should_continue = input("Do you want to continue? Y or N: "). upper()  # Option to end the game any time a word was found
            if should_continue == "N":
                print("Game over")
                break
            else:
                user_guess = input("Enter the word you spoted: ").lower()
                if user_guess in words_found: #  If word is already in words_found, let user know. It will not advance
                    # until word is different
                    print(f"{user_guess} was already found")
                else:
                    if user_guess in open_words_txt(): #  If word is different and is in txt file with words, then continue
                        print(f"You found the {user_guess}!")
                        letter_found_by_user = "" #  With this list, the function can compare the lenght of the word
                        # registered in user_guess with the lenght of this list. This will allow that the following while
                        # loop runs until letter_found_by_user has the same lenght as len(user_guess)
                        while len(letter_found_by_user) < len(user_guess):
                            letter_found = input("Enter the letter you found").lower()
                            row_location = int(input("Enter the row number")) - 1
                            column_location = int(input(" Enter the column number")) - 1
                            char_in_matrix = matrix[row_location][column_location] # It accesses to letter in the position
                            # registered in row_location and column_location
                            value_in_boolean_matrix = boolean_matrix[row_location][column_location] # It accesses to
                            # in the position registered in row_location and column_location
                            if letter_found == char_in_matrix and value_in_boolean_matrix:
                                print("Letter is correct")
                                letter_found_by_user += letter_found
                                matrix[row_location][column_location] = letter_found.upper()
                                print(create_matrix.fix_matrix(matrix))
                            else:
                                print("Letter is not correct")
                        words_found.append(user_guess)
                        print(f"You found of the letters of {user_guess}")
                    else:
                        print("Word not in alphabet soup")
        if len(words_found) == len(open_words_txt()):
            print("You found all the words")
            for word_found in open_words_txt():
                print(word_found)
        elif len(words_found) < len(open_words_txt()):
            print("You only found these words")
            for word_found in open_words_txt():
                print(word_found)
        else:
            print("No word was found")
    play_Game()


if __name__ == '__main__':
    main()  # Call main function
