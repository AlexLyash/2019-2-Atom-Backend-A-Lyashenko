import unittest
import re


class Game(object):

    def __init__(self):
        self.field = [['-' for x in range(3)] for x in range(3)]
        self.turn_flag = False
        self.size = 3

    def show_field(self):
        for i in range(self.size):
            for j in range(self.size):
                print('|' + 2*' ' + '{}'.format(self.field[i][j]) + 2*' ',
                      end='')
            print('|', end='')
            print('')
            print(19*'_')

    def turn(self, type_of_turn: str, coordinate: list):
        if self.field[coordinate[0]][coordinate[1]] != '-':
            return False

        if type_of_turn == 'cross':
            self.field[coordinate[0]][coordinate[1]] = 'X'
            return True
        elif type_of_turn == 'toe':
            self.field[coordinate[0]][coordinate[1]] = 'O'
            return True
        else:
            print('Input is wrong. Please enter cross or toe')
            return False

    def check_win(self):
        if ('-' != self.field[0][0] == self.field[1][1] == self.field[2][2]):
            return False
        elif ('-' != self.field[2][0] == self.field[1][1] == self.field[0][2]):
            return False
        else:
            for i in range(self.size):
                if ('-' != self.field[i][0] and
                        self.field[i].count(self.field[i][0]) == self.size):
                    return False
                elif ('-' != self.field[0][i] == self.field[1][i]
                        == self.field[2][i]):
                    return False
                else:
                    return True

    def play(self):
        self.turn_flag = True
        print('Game is started. Make your turn!')
        game_must_go_on = True
        while(game_must_go_on):
            stupidity_check = True
            while(stupidity_check):
                if (self.turn_flag):
                    x = input("It's cross turn. Enter coordinate as two numbers\
                              without spaces \n")
                    try:
                        coord = [int(y) for y in re.findall(r'\d{1}', x)]
                        self.turn('cross', coord)
                        stupidity_check = False
                    except IndexError:
                        print("Wrong data, try again!")
                        stupidity_check = True
                else:
                    try:
                        x = input("It's toe turn. Enter coordinate as two numbers\
                                  without spaces \n")
                        coord = [int(y) for y in re.findall(r'\d{1}', x)]
                        self.turn('toe', coord)
                    except IndexError:
                        print("Wrong data, try again!")
                        stupidity_check = True
            self.show_field()
            game_must_go_on = self.check_win()
            self.turn_flag = not self.turn_flag
        print('Game is over')
        if (self.turn_flag):
            print('toe wins!')
        else:
            print('cross wins')


class TestGame(unittest.TestCase):
    def test_check_win(self):
        self.field = [['-' for x in range(3)] for x in range(3)]
        game1.field[0][0] = game1.field[0][1] = game1.field[0][2] = 'X'
        self.assertEqual(game1.check_win(), False)
        self.field = [['-' for x in range(3)] for x in range(3)]
        game1.field[0][0] = game1.field[0][1] = game1.field[0][2] = 'O'
        self.assertEqual(game1.check_win(), False)
        self.field = [['-' for x in range(3)] for x in range(3)]
        game1.field[0][0] = game1.field[1][1] = game1.field[2][2] = 'X'
        self.assertEqual(game1.check_win(), False)
        self.field = [['-' for x in range(3)] for x in range(3)]
        game1.field[0][0] = game1.field[1][1] = game1.field[2][2] = 'X'
        self.assertEqual(game1.check_win(), False)
        self.field = [['-' for x in range(3)] for x in range(3)]
        game1.field[0][0] = game1.field[1][1] = game1.field[2][2] = 'O'
        self.assertEqual(game1.check_win(), False)


if __name__ == '__main__':
    game1 = Game()
    unittest.main()