def play_turn(game_board, x, y, piece):

    if 0 <= x <= 2 and 0 <= y <= 2:
        if game_board[y][x] == "":
            game_board[y][x] = piece
            return True
        else:
            return False
    else:
        return False
    
if __name__ == "__main__":
    
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)