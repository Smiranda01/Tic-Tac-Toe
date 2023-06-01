def display_board(game_board):
    for i, row in enumerate(game_board):
        print(" | ".join([f" {cell} " if cell != "" else "   " for cell in row]))
        if i < len(game_board) - 1:
            print("-" * 16)


def display_move_keys(move_dict):
    move_board = [["", "", ""], ["", "", ""], ["", "", ""]]

    for move, coordinates in move_dict.items():
        move_board[coordinates[0]][coordinates[1]] = move

    for i, row in enumerate(move_board):
        print(" | ".join([f" {cell} " if cell != "" else "   " for cell in row]))
        if i < len(move_board) - 1:
            print("-" * 45)


def check_win(game_board, players_dict, player):
    mark = players_dict[player]

    for row in game_board:
        if row.count(mark) == 3:
            return True

    for i in range(3):
        if [game_board[j][i] for j in range(3)].count(mark) == 3:
            return True

    if [game_board[i][i] for i in range(3)].count(mark) == 3 or [game_board[i][2 - i] for i in range(3)].count(
            mark) == 3:
        return True

    return False


def check_tie(game_board):
    for row in game_board:
        if "" in row:
            return False
    return True


def play():
    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]

    possible_moves = {
        "top left": [0, 0],
        "top center": [0, 1],
        "top right": [0, 2],
        "middle left": [1, 0],
        "center": [1, 1],
        "middle right": [1, 2],
        "bottom left": [2, 0],
        "bottom center": [2, 1],
        "bottom right": [2, 2],
    }
    players = {
        "Player 1": "X",
        "Player 2": "O"
    }

    game_on = True
    display_move_keys(possible_moves)
    print("")
    display_board(board)
    print("")

    while game_on:

        for player, mark in players.items():
            valid_move = False
            while not valid_move:
                move = input(f"{player} - '{mark}' choose your move\n").lower()

                try:
                    if board[possible_moves[move][0]][possible_moves[move][1]] == "":
                        board[possible_moves[move][0]][possible_moves[move][1]] = mark
                        if check_win(board, players, player):
                            print(f"{player} has won the game!")
                            print("")
                            display_board(board)
                            print("")
                            play_again = input("Do you wanna play again? Yes/No\n").title()
                            if play_again == "Yes":
                                play()
                            else:
                                return
                        else:
                            if check_tie(board):
                                print("That's a draw!")
                                print("")
                                display_board(board)
                                print("")
                                play_again = input("Do you wanna play again? Yes/No\n").title()
                                if play_again == "Yes":
                                    play()
                                else:
                                    return
                        print("")
                        display_board(board)
                        print("")
                        display_move_keys(possible_moves)
                        print("")
                        valid_move = True
                    else:
                        print(f"You cannot play {move} position as there is an {board[possible_moves[move][0]][possible_moves[move][1]]}")
                except KeyError as e:
                    print(f"Invalid move: {e}. Please try again.")


play()
