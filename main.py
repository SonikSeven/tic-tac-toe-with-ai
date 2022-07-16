from utils import Table
from utils import User
from utils import Computer


def main():
    table = Table()
    player_x, player_o = select_players()
    print(table)
    player = True
    while True:
        print(player_x.move(table) if player else player_o.move(table))
        player = not player
        status = table.get_status()
        if status != "Game not finished":
            return print(status)


def select_players(msg=""):
    players = "user", "easy", "medium", "hard"
    command = input(msg + "Input command: ")
    if command == "exit":
        exit()
    try:
        command, x, o = command.split()
        assert command == "start" and x in players and o in players
        return User("X") if x == "user" else Computer("X", x),\
               User("O") if o == "user" else Computer("O", o)
    except (ValueError, AssertionError):
        return select_players("Bad parameters!\n")


if __name__ == "__main__":
    main()
