from random import randint

HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]

letters_to_numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}


def print_board(board):
    print('    a b c d e f g h')
    print('    ---------------')
    row_number = 1
    for row in board:
        print("%d|%r|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'x':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'x'


def get_ship_location():
    row = input('Please enter a ship row 1-8')
    while row not in '12345678':
        print('Please enter a valid number')
        row = input('Please enter a ship row 1-8')
    column = input('Please enter a ship row a-h').lower()
    while column not in 'abcdefgh':
        print('Please enter a valid letter')
        column = input('Please enter a ship row a-h').lower()
    return int(row)-1, letters_to_numbers[column]


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'x':
                count += 1
    return count


create_ships(HIDDEN_BOARD)
turns = 10
print_board(HIDDEN_BOARD)
print_board(GUESS_BOARD)
# while turns > 0:
