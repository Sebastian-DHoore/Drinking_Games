import Card_game_classes
import os
import sys


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


def higher_lower(old, new, guess):
    if old.value > new.value:
        if guess == "Lower":
            return True
        else:
            return False
    elif old.value < new.value:
        if guess == "Higher":
            return True
        else:
            return False
    else:
        if guess == "On":
            return True
        else:
            return False


def in_out(left, middle, right, guess):
    if left.value < right.value:
        if left.value < middle.value < right.value:
            if guess == "in":
                return True
            else:
                return False
        elif left.value == middle.value or middle.value == right.value:
            if guess == "on":
                return True
            else:
                return False
        else:
            if guess == "out":
                return True
            else:
                return False
    elif left.value > right.value:
        if left.value > middle.value > right.value:
            if guess == "in":
                return True
            else:
                return False
        elif left.value == middle.value or middle.value == right.value:
            if guess == "on":
                return True
            else:
                return False
        else:
            if guess == "out":
                return True
            else:
                return False
    else:
        if left.value == middle.value:
            if guess == "on":
                return True
            else:
                return False
        else:
            if guess == "out":
                return True
            else:
                return False


class Board(object):
    def __init__(self):
        self.row_1_left = []
        self.row_1_middle = None
        self.row1right = []
        self.row_1 = False
        self.row2left = []
        self.row2middle = None
        self.row2right = []
        self.row_2 = False
        self.row3left = []
        self.row3middle = None
        self.row3right = []
        self.row_3 = False
        self.deck = None
        self.build()

    def build(self):
        self.deck = Card_game_classes.Deck()
        self.deck.shuffle()
        self.row_1_left.append(self.deck.deal())
        self.row_1_middle = self.deck.deal()
        self.row_1_middle.showing = False
        self.row1right.append(self.deck.deal())
        self.row2left.append(self.deck.deal())
        self.row2middle = self.deck.deal()
        self.row2middle.showing = False
        self.row2right.append(self.deck.deal())
        self.row3left.append(self.deck.deal())
        self.row3middle = self.deck.deal()
        self.row3middle.showing = False
        self.row3right.append(self.deck.deal())

    def show(self):
        printable1 = self.row_1_left[::-1]
        printable2 = self.row2left[::-1]
        printable3 = self.row3left[::-1]
        print(*printable1, "|", self.row_1_middle, "|", *self.row1right)
        print(*printable2, "|", self.row2middle, "|", *self.row2right)
        print(*printable3, "|", self.row3middle, "|", *self.row3right)

    def reveal(self, row, guess, player):
        if row == 1:
            self.row_1_middle.showing = True
            print()
            print("Middle of row {} is {}".format(row, guess))
            print()
            printable1 = self.row_1_left[::-1]
            print(*printable1, "|", self.row_1_middle, "|", *self.row1right)
            print()
            if in_out(self.row_1_left[0], self.row_1_middle, self.row1right[0], guess):
                print("That was right, this is the new board")
                print()
                self.show()
                self.row_1 = True
                print()
                return True
            else:
                print("That was wrong, this is the new board")
                print()
                self.row_1 = True
                self.replace(self.row_1_left, 1, "left", player)
                self.show()
                print()
                return False
        elif row == 2:
            self.row2middle.showing = True
            print()
            print("Middle of row {} is {}".format(row, guess))
            print()
            printable2 = self.row2left[::-1]
            print(*printable2, "|", self.row2middle, "|", *self.row2right)
            print()
            if in_out(self.row2left[0], self.row2middle, self.row2right[0], guess):
                print("That was right, this is the new board")
                print()
                self.row_2 = True
                self.show()
                print()
                return True
            else:
                print("That was wrong, this is the new board")
                print()
                self.row_2 = True
                self.replace(self.row2left, 2, "left", player)
                self.show()
                print()
                return False
        else:
            self.row3middle.showing = True
            print()
            print("Middle of row {} is {}".format(row, guess))
            print()
            printable3 = self.row3left[::-1]
            print(*printable3, "|", self.row3middle, "|", *self.row3right)
            print()
            if in_out(self.row3left[0], self.row3middle, self.row3right[0], guess):
                print("That was right, this is the new board")
                print()
                self.row_3 = True
                self.show()
                print()
                return True
            else:
                print("That was wrong, this is the new board")
                print()
                self.row_3 = True
                self.replace(self.row3left, 3, "left", player)
                self.show()
                print()
                return False

    def place(self, draw, row, side, guess, player):

        if row == 1 and side == "left":
            print()
            print("{} than {} on the {} of row {}".format(guess, self.row_1_left[len(self.row_1_left) - 1], side, row))
            print()
            if guess == "Higher":
                print("{} > {}".format(draw, self.row_1_left[len(self.row_1_left) - 1]))
            elif guess == "Lower":
                print("{} < {}".format(draw, self.row_1_left[len(self.row_1_left) - 1]))
            else:
                print("{} = {}".format(draw, self.row_1_left[len(self.row_1_left) - 1]))
            print()
            if higher_lower(self.row_1_left[len(self.row_1_left) - 1], draw, guess):
                print("That was right, this is the new board")
                print()
                self.row_1_left.append(draw)
                self.show()
                print()
                return True
            else:
                print("That was wrong, this is the new board")
                print()
                self.deck.refill(draw)
                self.replace(self.row_1_left, 1, "left", player)
                self.show()
                print()
                return False
        elif row == 1 and side == "right":
            print()
            print("{} than {} on the {} of row {}".format(guess, self.row1right[len(self.row1right) - 1], side, row))
            print()
            if guess == "Higher":
                print("{} > {}".format(draw, self.row1right[len(self.row1right) - 1]))
            elif guess == "Lower":
                print("{} < {}".format(draw, self.row1right[len(self.row1right) - 1]))
            else:
                print("{} = {}".format(draw, self.row1right[len(self.row1right) - 1]))
            print()
            if higher_lower(self.row1right[len(self.row1right) - 1], draw, guess):
                print("That was right, this is the new board")
                print()
                self.row1right.append(draw)
                self.show()
                print()
                return True
            else:
                print("That was wrong, this is the new board")
                print()
                self.deck.refill(draw)
                self.replace(self.row1right, 1, "right", player)
                self.show()
                print()
                return False
        elif row == 2 and side == "left":
            print()
            print("{} than {} on the {} of row {}".format(guess, self.row2left[len(self.row2left) - 1], side, row))
            print()
            if guess == "Higher":
                print("{} > {}".format(draw, self.row2left[len(self.row2left) - 1]))
            elif guess == "Lower":
                print("{} < {}".format(draw, self.row2left[len(self.row2left) - 1]))
            else:
                print("{} = {}".format(draw, self.row2left[len(self.row2left) - 1]))
            print()
            if higher_lower(self.row2left[len(self.row2left) - 1], draw, guess):
                print("That was right, this is the new board")
                print()
                self.row2left.append(draw)
                self.show()
                print()
                return True
            else:
                print("That was wrong, this is the new board")
                print()
                self.deck.refill(draw)
                self.replace(self.row2left, 2, "left", player)
                self.show()
                print()
                return False
        elif row == 2 and side == "right":
            print()
            print("{} than {} on the {} of row {}".format(guess, self.row2right[len(self.row2right) - 1], side, row))
            print()
            if guess == "Higher":
                print("{} > {}".format(draw, self.row2right[len(self.row2right) - 1]))
            elif guess == "Lower":
                print("{} < {}".format(draw, self.row2right[len(self.row2right) - 1]))
            else:
                print("{} = {}".format(draw, self.row2right[len(self.row2right) - 1]))
            print()
            if higher_lower(self.row2right[len(self.row2right) - 1], draw, guess):
                print("That was right, this is the new board")
                print()
                self.row2right.append(draw)
                self.show()
                print()
                return True
            else:
                print("That was wrong, this is the new board")
                print()
                self.deck.refill(draw)
                self.replace(self.row2right, 2, "right", player)
                self.show()
                print()
                return False
        elif row == 3 and side == "left":
            print()
            print("{} than {} on the {} of row {}".format(guess, self.row3left[len(self.row3left) - 1], side, row))
            print()
            if guess == "Higher":
                print("{} > {}".format(draw, self.row3left[len(self.row3left) - 1]))
            elif guess == "Lower":
                print("{} < {}".format(draw, self.row3left[len(self.row3left) - 1]))
            else:
                print("{} = {}".format(draw, self.row3left[len(self.row3left) - 1]))
            print()
            if higher_lower(self.row3left[len(self.row3left) - 1], draw, guess):
                print("That was right, this is the new board")
                print()
                self.row3left.append(draw)
                self.show()
                print()
                return True
            else:
                print("That was wrong, this is the new board")
                print()
                self.deck.refill(draw)
                self.replace(self.row3left, 3, "left", player)
                self.show()
                print()
                return False
        else:
            print()
            print("{} than {} on the {} of row {}".format(guess, self.row3right[len(self.row3right) - 1], side, row))
            print()
            if guess == "Higher":
                print("{} > {}".format(draw, self.row3right[len(self.row3right) - 1]))
            elif guess == "Lower":
                print("{} < {}".format(draw, self.row3right[len(self.row3right) - 1]))
            else:
                print("{} = {}".format(draw, self.row3right[len(self.row3right) - 1]))
            print()
            if higher_lower(self.row3right[len(self.row3right) - 1], draw, guess):
                print("That was right, this is the new board")
                print()
                self.row3right.append(draw)
                self.show()
                print()
                return True
            else:
                print("That was wrong, this is the new board")
                print()
                self.deck.refill(draw)
                self.replace(self.row3right, 3, "right", player)
                self.show()
                print()
                return False

    def replace(self, row_segment, row, side, player):
        if row == 1:
            if self.row_1:
                shots = len(self.row_1_left) + len(self.row1right) + 1
                player.drink(shots)
                for f in range(0, len(self.row_1_left)):
                    self.deck.refill(self.row_1_left[f])
                for f in range(0, len(self.row1right)):
                    self.deck.refill(self.row1right[f])
                self.deck.refill(self.row_1_middle)
                self.row_1_left = []
                self.row_1_middle = None
                self.row1right = []
                self.row_1 = False
                self.row_1_left.append(self.deck.deal())
                self.row_1_middle = self.deck.deal()
                self.row_1_middle.showing = False
                self.row1right.append(self.deck.deal())
            else:
                shots = len(row_segment) + 1
                player.drink(shots)
                for f in range(0, len(row_segment)):
                    self.deck.refill(row_segment[f])
                if side == "left":
                    self.row_1_left = [self.deck.deal()]
                else:
                    self.row1right = [self.deck.deal()]
        elif row == 2:
            if self.row_2:
                shots = len(self.row2left) + len(self.row2right) + 1
                player.drink(shots)
                for f in range(0, len(self.row2left)):
                    self.deck.refill(self.row2left[f])
                for f in range(0, len(self.row2right)):
                    self.deck.refill(self.row2right[f])
                self.deck.refill(self.row2middle)
                self.row2left = []
                self.row2middle = None
                self.row2right = []
                self.row_2 = False
                self.row2left.append(self.deck.deal())
                self.row2middle = self.deck.deal()
                self.row2middle.showing = False
                self.row2right.append(self.deck.deal())
            else:
                shots = len(row_segment) + 1
                player.drink(shots)
                for f in range(0, len(row_segment)):
                    self.deck.refill(row_segment[f])
                if side == "left":
                    self.row2left = [self.deck.deal()]
                else:
                    self.row2right = [self.deck.deal()]
        else:
            if self.row_3:
                shots = len(self.row3left) + len(self.row3right) + 1
                player.drink(shots)
                for f in range(0, len(self.row3left)):
                    self.deck.refill(self.row3left[f])
                for f in range(0, len(self.row3right)):
                    self.deck.refill(self.row3right[f])
                self.deck.refill(self.row3middle)
                self.row3left = []
                self.row3middle = None
                self.row3right = []
                self.row_3 = False
                self.row3left.append(self.deck.deal())
                self.row3middle = self.deck.deal()
                self.row3middle.showing = False
                self.row3right.append(self.deck.deal())
            else:
                shots = len(row_segment) + 1
                player.drink(shots)
                for f in range(0, len(row_segment)):
                    self.deck.refill(row_segment[f])
                if side == "left":
                    self.row3left = [self.deck.deal()]
                else:
                    self.row3right = [self.deck.deal()]


class DrinkingGame(object):
    def __init__(self):
        self.players = []
        self.current_player = None
        self.board = None
        self.game_end = False
        self.build()

    def build(self):
        bas = Card_game_classes.Player("Bas")
        giel = Card_game_classes.Player("Giel")
        brently = Card_game_classes.Player("Brently")
        gijs = Card_game_classes.Player("Gijs")
        self.players = [bas, giel, brently, gijs]
        self.current_player = self.players[0]
        self.board = Board()

    def start(self):
        print()
        print("These are the starting players:")
        print()
        for x in range(0, len(self.players)):
            self.players[x].show_without_turnstreak()
        print()
        print("This is the starting board")
        print()
        self.board.show()

    def turn(self, row, guess, side=None):
        if side is None:
            boolean = self.board.reveal(row, guess, self.current_player)
        else:
            boolean = self.board.place(self.board.deck.deal(), row, side, guess, self.current_player)
        if boolean is True:
            self.current_player.turnstreak_up()
            self.current_player.turn_up()
        else:
            self.current_player.turnstreak_reset()
            self.current_player.turn_up()
        if not myGame.board.deck.cards:
            if (self.board.row_1 is True) and (self.board.row_2 is True) and (self.board.row_3 is True):
                self.game_end = True
                return
        self.current_player.show()
        if self.current_player.turnstreak == 3:
            self.current_player.turnstreak_reset()
            index = self.players.index(self.current_player)
            if index < len(self.players) - 1:
                print()
                print("{} passed the turn to {}".format(self.current_player.name, self.players[index + 1].name))
                self.current_player = self.players[index + 1]
            else:
                print()
                print("{} passed the turn to {}".format(self.current_player.name, self.players[0].name))
                self.current_player = self.players[0]

    def end(self):
        for x in range(0, len(self.players)):
            self.players[x].show_without_turnstreak()
        print()
        print("The game took {} turns".
              format
              (myGame.players[0].turns + myGame.players[1].turns + myGame.players[2].turns + myGame.players[3].turns))
        print()
        print("The players took {} shots".
              format
              (myGame.players[0].shots + myGame.players[1].shots + myGame.players[2].shots + myGame.players[3].shots))

    def best_move(self):

        guess1, row1, side1, best_high_low_chance = None, None, None, None

        if myGame.board.deck.cards:
            high_low = (self.board.row_1_left[len(self.board.row_1_left) - 1].value,
                        self.board.row1right[len(self.board.row1right) - 1].value,
                        self.board.row2left[len(self.board.row2left) - 1].value,
                        self.board.row2right[len(self.board.row2right) - 1].value,
                        self.board.row3left[len(self.board.row3left) - 1].value,
                        self.board.row3right[len(self.board.row3right) - 1].value)
            high_low_place = ((1, "left"), (1, "right"), (2, "left"), (2, "right"), (3, "left"), (3, "right"))

            higher_chance = []
            lower_chance = []
            on_chance = []

            for i in high_low:

                counter = 0
                for j in range(i + 1, 14):
                    for k in range(0, len(self.board.deck.cards)):
                        if j == self.board.deck.cards[k].value:
                            counter += 1
                higher_chance.append(counter / len(self.board.deck.cards))

                counter = 0
                for j in range(i - 1, 0, -1):
                    for k in range(0, len(self.board.deck.cards)):
                        if j == self.board.deck.cards[k].value:
                            counter += 1
                lower_chance.append(counter / len(self.board.deck.cards))

                counter = 0
                for k in range(0, len(self.board.deck.cards)):
                    if i == self.board.deck.cards[k].value:
                        counter += 1
                on_chance.append(counter / len(self.board.deck.cards))

            # test
            # total_high_low_chance = []
            # for f in range(0, len(higher_chance)):
            #     total_high_low_chance.append(higher_chance[f] + lower_chance[f] + on_chance[f])

            best_higher_chance = max(higher_chance)
            best_lower_chance = max(lower_chance)
            best_on_chance = max(on_chance)

            if best_higher_chance >= best_lower_chance and best_higher_chance >= best_on_chance:
                best_high_low_chance = best_higher_chance
                best_high_low_index = higher_chance.index(best_higher_chance)
                guess1 = "Higher"
            elif best_lower_chance >= best_higher_chance and best_lower_chance >= best_on_chance:
                best_high_low_chance = best_lower_chance
                best_high_low_index = lower_chance.index(best_lower_chance)
                guess1 = "Lower"
            else:
                best_high_low_chance = best_on_chance
                best_high_low_index = on_chance.index(best_on_chance)
                guess1 = "On"

            row1, side1 = high_low_place[best_high_low_index]

        left = (self.board.row_1_left[0].value, self.board.row2left[0].value, self.board.row2left[0].value)
        right = (self.board.row1right[0].value, self.board.row2right[0].value, self.board.row3right[0].value)
        is_flipped = (self.board.row_1, self.board.row_2, self.board.row_3)
        in_out_place = ((1, None), (2, None), (3, None))

        in_chance = []
        out_chance = []
        in_out_on_chance = []

        for g in range(0, len(left)):
            i, j, v = left[g], right[g], is_flipped[g]
            if not v:

                i_and_j = [i, j]
                i = min(i_and_j)
                j = max(i_and_j)

                counter = 0
                for k in range(i + 1, j):
                    for m in range(0, len(self.board.deck.cards)):
                        if k == self.board.deck.cards[m].value:
                            counter += 1
                in_chance.append(counter / len(self.board.deck.cards))

                counter = 0
                for k in range(i - 1, 0, -1):
                    for m in range(0, len(self.board.deck.cards)):
                        if k == self.board.deck.cards[m].value:
                            counter += 1
                for k in range(j + 1, 14):
                    for m in range(0, len(self.board.deck.cards)):
                        if k == self.board.deck.cards[m].value:
                            counter += 1
                out_chance.append(counter / len(self.board.deck.cards))

                counter = 0
                for m in range(0, len(self.board.deck.cards)):
                    if i == self.board.deck.cards[m].value:
                        counter += 1
                in_out_on_chance.append(counter / len(self.board.deck.cards))
            else:
                in_chance.append(0)
                out_chance.append(0)
                in_out_on_chance.append(0)

        # test
        # total_in_out_chance = []
        # for f in range(0, len(higher_chance)):
        #     total_in_out_chance.append(higher_chance[f] + lower_chance[f] + on_chance[f])

        best_in_chance = max(in_chance)
        best_out_chance = max(out_chance)
        best_in_out_on_chance = max(in_out_on_chance)

        if best_in_chance >= best_out_chance and best_in_chance >= best_in_out_on_chance:
            best_in_out_chance = best_in_chance
            best_in_out_index = in_chance.index(best_in_chance)
            guess2 = "in"
        elif best_out_chance >= best_in_chance and best_out_chance >= best_in_out_on_chance:
            best_in_out_chance = best_out_chance
            best_in_out_index = out_chance.index(best_out_chance)
            guess2 = "out"
        else:
            best_in_out_chance = best_in_out_on_chance
            best_in_out_index = in_out_on_chance.index(best_in_out_on_chance)
            guess2 = "on"

        row2, side2 = in_out_place[best_in_out_index]

        if myGame.board.deck.cards:
            if best_high_low_chance > best_in_out_chance:
                row, side, guess = row1, side1, guess1
            else:
                row, side, guess = row2, side2, guess2
        else:
            row, side, guess = row2, side2, guess2
        return row, side, guess

    def make_best_move(self):
        row, side, guess = self.best_move()
        self.turn(row, guess, side)


# Simulation

with HiddenPrints():
    while 1:
        myGame = DrinkingGame()
        myGame.start()
        while not myGame.game_end:
            myGame.make_best_move()
        myGame.end()
        file1 = 'Drinking_game_data/Turns.txt'
        file2 = 'Drinking_game_data/Shots.txt'
        with open(file1, 'a') as filetowrite:
            filetowrite.write(
                str(myGame.players[0].turns + myGame.players[1].turns
                    + myGame.players[2].turns + myGame.players[3].turns))
            filetowrite.write(", ")
        with open(file2, 'a') as filetowrite:
            filetowrite.write(
                str(myGame.players[0].shots + myGame.players[1].shots
                    + myGame.players[2].shots + myGame.players[3].shots))
            filetowrite.write(", ")
