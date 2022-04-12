

class X_O_game:

    
    empty = ''

    def __init__(self):

        self.board = [
            [X_O_game.empty,X_O_game.empty,X_O_game.empty],
            [X_O_game.empty,X_O_game.empty,X_O_game.empty],
            [X_O_game.empty,X_O_game.empty,X_O_game.empty]
        ]

        self.current_player = 'X'

    def draw_board(self):
        print(' | '.join(self.board[0]))
        print(' | '.join(self.board[1]))
        print(' | '.join(self.board[2]))

    def play_next_move(self, move):
        i, j = move[0], move[1]

        self.board[i][j] = self.current_player

        if self.current_player == 'X':
            self.current_player = 'O'
        elif self.current_player == 'O':
            self.current_player = 'X'

    def valid_move(self, move):
        i, j = move[0], move[1]

        if i not in [0,1,2] or j not in [0,1,2] or self.board[i][j] == 'X' or self.board == 'O':
            return False
        
        return True


def find_empty_space(board):

    for i in range(3):
        for j in range(3):
            if board[i][j] == X_O_game.empty:
                return True
    
    return False




def tie_game(game):

    winner = get_winner(game)

    if winner is None and not find_empty_space(game.board):
        return True
    
    return False


def get_winner(game):

    board = game.board

    for i in range(3):
        if board[i][0] == board [i][1] == board[i][2] and board[i][0]!=X_O_game.empty:
            return board[i][0]

    
    for i in range(3):
        if board[0][i] == board [1][i] == board[2][i]  and board[0][i]!=X_O_game.empty:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0]!=X_O_game.empty:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][0]!=X_O_game.empty:
        return board[1][1]
    
    return None

def get_next_move():
    move = input().split(',')
    return [int(move[0]), int(move[1])]



game = X_O_game()
game.draw_board()

while True:
    next_move = get_next_move()
    if not game.valid_move(next_move):
        print('Move is not valid!')
        break
    game.play_next_move(next_move)
    game.draw_board()

    if get_winner(game) == 'X':
        print('Player X wins')
        break

    if tie_game(game):
        print('Tie')
        break

    if get_winner(game) == 'Y':
        print('Player Y won')
        break


# move = get_move
# if game.valid_move(move):
# continue
# else :
# print('Greska')
# move = get_move (...)