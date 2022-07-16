import random


class Table(list):
    combinations = ({0, 1, 2}, {3, 4, 5}, {6, 7, 8},
                    {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
                    {0, 4, 8}, {2, 4, 6})

    def __init__(self):
        super().__init__(" " * 9)

    def __str__(self):
        return " ".join(("---------",
                         "\n|", *self[:3], "|",
                         "\n|", *self[3:6], "|",
                         "\n|", *self[6:], "|",
                         "\n---------"))

    def get_positions(self, char):
        return {index for index, element in enumerate(self) if element == char}

    def get_status(self):
        for a, b, c in self.combinations:
            if self[a] == self[b] == self[c] != " ":
                return f"{self[a]} wins"
        if self.count(" ") == 0:
            return "Draw"
        return "Game not finished"


class User:
    def __init__(self, char):
        self.char = char

    def move(self, table, msg=""):
        try:
            x, y = (int(i) - 1 for i in input(msg + "Enter the coordinates: ").split())
            index = x * 3 + y
            if x > 2 or y > 2:
                msg = "Coordinates should be from 1 to 3!\n"
            elif table[index] != " ":
                msg = "This cell is occupied! Choose another one!\n"
            else:
                table[index] = self.char
                return table
        except ValueError:
            msg = "You should enter numbers!\n"
        return self.move(table, msg)


class Computer:
    def __init__(self, char, difficulty):
        self.char = char
        self.difficulty = difficulty
        self.enemy_char = "X" if self.char == "O" else "O"

    def move(self, table):
        print(f'Making move level "{self.difficulty}"')
        enemy = table.get_positions(self.enemy_char)
        empty = table.get_positions(" ")

        if self.difficulty == "hard":
            best_score = -10000
            best_move = 0
            for i in empty:
                table[i] = self.char
                score = self.minimax(table)
                table[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
            table[best_move] = self.char
            return table
        elif self.difficulty == "medium":
            for i in table.combinations:
                if len(i & enemy) == 2 and len(i & empty) == 1:
                    (i,) = i & empty
                    table[i] = self.char
                    return table
        index = random.choice(tuple(empty))
        table[index] = self.char
        return table

    def minimax(self, table, switcher=False):
        empty = table.get_positions(" ")
        status = table.get_status()

        if status[0] == self.char:
            return 10
        elif status[0] == self.enemy_char:
            return -10
        elif status == "Draw":
            return 0

        if switcher:
            best_score = -10000
            for i in empty:
                table[i] = self.char
                score = self.minimax(table, False)
                table[i] = " "
                if score > best_score:
                    best_score = score
            return best_score
        else:
            best_score = 10000
            for i in empty:
                table[i] = self.enemy_char
                score = self.minimax(table, True)
                table[i] = " "
                if score < best_score:
                    best_score = score
            return best_score
