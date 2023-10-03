#noughts_crosses.py v1.0.0

import sys
import random

class game:

    # declares a list which contains the playable pieces
    def __init__(self):
        self.pieces = ["X", "O", "x", "o"]
        
    
    # contains the 8 winning lines which get refreshed when the function
    # is called.
    def win_line_refresh(self):
        self.l123 = [grid_content[0], grid_content[1], grid_content[2]]
        self.l456 = [grid_content[3], grid_content[4], grid_content[5]]
        self.l789 = [grid_content[6], grid_content[7], grid_content[8]]
        self.l147 = [grid_content[0], grid_content[3], grid_content[6]]
        self.l258 = [grid_content[1], grid_content[4], grid_content[7]]
        self.l369 = [grid_content[2], grid_content[5], grid_content[8]]
        self.l159 = [grid_content[0], grid_content[4], grid_content[8]]
        self.l357 = [grid_content[2], grid_content[4], grid_content[6]]
    
    # The following function prints the current board to the command window.
    def print_board(self, board):
        print()
        print(board[:3])
        print(board[3:6])
        print(board[6:])
        print()
        
    # This function takes the existing board, position input from player,
    # marker type (either X, O, x or o) and returns the updated board based
    # on the arguments.
    def draw_board(self, board, position, marker):
        board[position-1] = marker
        g.print_board(board)
        return board

    # The user inputs whether they want to play against another person or the
    # computer.
    def startup(self):
        self.answer = input("\nPlease respond with either \"p\" for person \
or \"c\" for computer.\n>>> ")
        if self.answer == "p":
            g.person()
        elif self.answer == "c":
            g.computer()
        else:
            g.startup()

    # This function contains the loop of play when two humans are playing.
    def person(self):
        while play_count != 9:
            print("\nPlayer 1, would you like to place an \"X\" or an \"O\"?")
            g.player1_piece()
            g.player1_pos()
            g.game_state_p1()
            g.count_state()
            print("\nPlayer 2, would you like to place an \"X\" or an \"O\"?")
            g.player2_piece()
            g.player2_pos()
            g.game_state_p2()
            g.count_state()

    # This is the function that contains the loop of play when it is human
    # vs. computer.
    def computer(self):
        while play_count != 9:
            print("\nPlayer 1, would you like to place an \"X\" or an \"O\"?")
            g.player1_piece()
            g.player1_pos()
            g.game_state_p1()
            g.count_state()
            g.comp()
            print("\nThe computer places an \"O\" in position \
"+self.comp_pos+".")
            print()
            g.game_state_comp()
            g.count_state()

    # player 1 chooses which piece to put on the board.
    def player1_piece(self):
        self.p1_piece = input(">>> ")
        if not self.p1_piece in self.pieces:
            print("\nPlease enter either an \"X\" or an \"O\". It can be \
uppercase\nor lowercase.")
            g.player1_piece()
            

    # Player 1 then chooses where the piece will be played. the number of
    # plays then increases by one, the new board is drawn in the terminal, and
    # that played position is stored to be compared by the refreshed winning
    # lines function.
    def player1_pos(self):
        p1_pos = input("\nIn which position would you like to place \
your piece?\n>>> ")
        if p1_pos in position:
            position_num = position.index(p1_pos)
            del position[position_num]
            g.draw_board(board, int(p1_pos), self.p1_piece)
            global play_count
            play_count = play_count + 1
            grid_content[int(p1_pos)-1] = "p1"
            g.win_line_refresh()
        else:
            print("\nPlease enter a NUMBERED position that is EMPTY. ")
            g.player1_pos()

    # Player 2 chooses their piece to be played. 
    def player2_piece(self):
        self.p2_piece = input(">>> ")
        if not self.p2_piece in self.pieces:
            print("\nPlease enter either an \"X\" or an \"O\". It can be \
uppercase\nor lowercase.")
            g.player2_piece()

    # Just like for the function similar for player 1, player 2's play position
    # is stored, the number of plays increases by one, and the winning lines are
    # refreshed.
    def player2_pos(self):
        p2_pos = input("\nPlayer 2, in which position would you like to \
place your 'O'?\n>>> ")
        if p2_pos in position:
            position_num = position.index(p2_pos)
            del position[position_num]
            g.draw_board(board, int(p2_pos), self.p2_piece)
            global play_count
            play_count = play_count + 1
            grid_content[int(p2_pos)-1] = "p2"
            g.win_line_refresh()
        else:
            print("\nPlease enter a NUMBERED position that is EMPTY. ")
            g.player2_pos()
            
    # the computer then plays. This has the same functionality as player 1 and
    # player 2's plays.
    def comp(self):
        self.comp_pos = random.choice(position)
        position_num = position.index(self.comp_pos)
        del position[position_num]
        g.draw_board(board, int(self.comp_pos), "O")
        global play_count
        play_count = play_count + 1
        grid_content[int(self.comp_pos)-1] = "O"
        g.win_line_refresh()

    # This function checks whether player 1 has filled up any of the winning
    # lines, thus winning the game.
    def game_state_p1(self):
        if all(i == "p1" for i in self.l123):
                g.p1_win()
        elif all(i == "p1" for i in self.l456):
                g.p1_win()
        elif all(i == "p1" for i in self.l789):
                g.p1_win()
        elif all(i == "p1" for i in self.l147):
                g.p1_win()
        elif all(i == "p1" for i in self.l258):
                g.p1_win()
        elif all(i == "p1" for i in self.l369):
                g.p1_win()
        elif all(i == "p1" for i in self.l159):
                g.p1_win()
        elif all(i == "p1" for i in self.l357):
                g.p1_win()

    # player 2's moves are checked to see if player 2 has won or not.
    def game_state_p2(self):
        if all(i == "p2" for i in self.l123):
                g.p2_win()
        elif all(i == "p2" for i in self.l456):
                g.p2_win()
        elif all(i == "p2" for i in self.l789):
                g.p2_win()
        elif all(i == "p2" for i in self.l147):
                g.p2_win()
        elif all(i == "p2" for i in self.l258):
                g.p2_win()
        elif all(i == "p2" for i in self.l369):
                g.p2_win()
        elif all(i == "p2" for i in self.l159):
                g.p2_win()
        elif all(i == "p2" for i in self.l357):
                g.p2_win()

    # This function sees if the computer has won or not.
    def game_state_comp(self):
        if all(i == "O" for i in self.l123):
                g.comp_win()
        elif all(i == "O" for i in self.l456):
                g.comp_win()
        elif all(i == "O" for i in self.l789):
                g.comp_win()
        elif all(i == "O" for i in self.l147):
                g.comp_win()
        elif all(i == "O" for i in self.l258):
                g.comp_win()
        elif all(i == "O" for i in self.l369):
                g.comp_win()
        elif all(i == "O" for i in self.l159):
                g.comp_win()
        elif all(i == "O" for i in self.l357):
                g.comp_win()

    # When this function is called in the play loop, it checks to see if the
    # number of plays has reached nine. If so, the game is a tie, and the program
    # terminates.
    def count_state(self):
        global play_count
        if play_count == 9:
            print("It's a tie!\nThank you for playing.")
            sys.exit()
            
    # When player 1 wins, this function is called, tells to user so, and exits
    # the program.
    def p1_win(self):
        print("\nCongratulations player 1, you win!")
        sys.exit()

    # A message is displayed telling the user that player 2 has won, and the ends
    # the program.
    def p2_win(self):
        print("\nCongratulations player 2, you win!")
        sys.exit()
        
    # If the computer wins, this message is displayed, and terminates the
    # program.
    def comp_win(self):
        print("\nOh dear... It seems as though the computer has beaten \
the human!")
        sys.exit()
        
    
    
   
# This is the program main where key variables/lists are stored. The class "game"
# is shortened to "g" also.
board = [".",".",".",".",".",".",".",".","."]
grid_content = [".",".",".",".",".",".",".",".","."]
position = ['1','2','3','4','5','6','7','8','9']
play_count = 0
g = game()


# This message greets the player, prints the board wih labelled positions, and an
# empty board, asks them if they want to play with another person or the
# computer, and then begins the game.
print("\nHello, and welcome to 'Noughts and Crosses'!\n\nBelow, you will see \
a board with the positions numbered for you. You must take \nit \
in turns to place either an 'X' or an 'O' on the board, and the first to get a \
horizontal, vertical or diagonal line of their letter wins!")
g.print_board(position)
print()
print("Here is your playing board:")
print()
g.print_board(board)
print()
print("Would you like to play against another person \
or the computer?")
g.startup()

