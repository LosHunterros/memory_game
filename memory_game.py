import os
import random


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_board(width, height):
    letters_needed = int(height * width / 2)
    if letters_needed > len(alphabet): raise ValueError("To large board")
    if ( height * width ) % 2 == 1: raise ValueError("Wrong amount of fields")

    alphabet_new = alphabet[0:letters_needed]
    alphabet_new = alphabet_new * 2

    alphabet_list = []
    for char in alphabet_new:
        alphabet_list.append(char)

    random.shuffle(alphabet_list)

    matrix = []

    for i in range(height):
        matrix.append([])
        for j in range(width):
            matrix[i].append(alphabet_list.pop())

    return matrix


def main():
    # write your code here
    print(generate_board(4, 2))


if __name__ == "__main__":
    main()