BOARD_LONG = 6
BOARD_WEDTH = 7
class Game:

    def __init__(self):
        """
        __board : game board
        __turn : player turn (turn=1 player 1,turn=-1 player 2)
        __colon_row_player:
        __winner_cord_lst :list of the winner cords
        """
        self.__board = self.__bigen_board()
        self.__turn = 1
        self.__colon_row_player=[]
        self.__winner_cord_lst = []


    def get_winner_cord_lst(self):
        """
        getter
        :return:list of the winner cords
        """
        return self.__winner_cord_lst


    def board(self):
        """
        getter
        :return: board
        """
        return self.__board


    def __bigen_board(self):
        """
        :return:make empty board
        """
        lst = []
        for i in range(BOARD_WEDTH):
            lst.append([])
            for j in range(BOARD_LONG):
                lst[i].append(None)
        return lst


    def make_move(self, column):
        """
        make move and save it in the board
        :param column: column to but disck in
        :return: Illegal move if it is illegal move else None
        """
        if self.get_winner() is not None :
            return

        self.__turn *= -1
        for i in range(BOARD_LONG):
            if self.__board[column][-(i+1)] is None :
                if self.get_current_player() == 2:
                    self.__board[column][-(i+1)] = True
                    self.colon_row_player = [(column,BOARD_LONG-i),1]
                    return
                else:
                    self.__board[column][-(i+1)] = False
                    self.colon_row_player = [(column, BOARD_LONG - i), 2]
                    return
        return "Illegal move"


    def __search_in_dirction_d(self,i,j):
        """
        search win in down dirction
        :param i: colon to start
        :param j: row to start
        :return: 1 if player 1 got win 2 if player 2 win else None
        """
        count_1 = 0
        count_2 = 0
        lst = []
        for k in range(min(BOARD_LONG-j,4)):
            if self.__board[i][j+k] :
                lst.append((i,j+k+1))
                count_1 +=1
            else:
                lst.append((i, j + k + 1))
                count_2 +=1
            if count_1 >3 :
                self.__winner_cord_lst = lst
                return 1
            if count_2 >3:
                self.__winner_cord_lst = lst
                return 2


    def __search_in_dirction_r(self, i, j):
        """
        search win in right dirction
        :param i: colon to start
        :param j: row to start
        :return: 1 if player 1 got win 2 if player 2 win else None
        """
        count_1 = 0
        count_2 = 0
        lst= []
        for k in range(min(BOARD_WEDTH - i,4)):
            if self.__board[i+k][j] is not None:
                if self.__board[i+k][j]:
                    lst.append((i+k,j+1))
                    count_1 += 1
                else:
                    lst.append((i + k, j+1))
                    count_2 += 1
                if count_1 > 3:
                    self.__winner_cord_lst = lst
                    return 1
                if count_2 > 3:
                    self.__winner_cord_lst = lst
                    return 2


    def __search_in_dirction_x(self, i, j):
        """
        search win in diagonal /  dirction
        :param i: colon to start
        :param j: row to start
        :return: 1 if player 1 got win 2 if player 2 win else None
        """
        count_1 = 0
        count_2 = 0
        lst = []
        for k in range(min (BOARD_WEDTH - i,BOARD_LONG - j,4)):
            if self.__board[i + k][j+k] is not None:
                if self.__board[i + k][j+k]:
                    lst.append((i+k,j+k+1))
                    count_1 += 1
                else:
                    lst.append((i + k, j + k + 1))
                    count_2 += 1
                if count_1 > 3:
                    self.__winner_cord_lst = lst
                    return 1
                if count_2 > 3:
                    self.__winner_cord_lst = lst
                    return 2


    def __check_tiko(self):
        """
        :return: True if its not tiko else False
        """
        for i in range(BOARD_WEDTH):
            for j in range(BOARD_LONG):
                if self.__board[i][j] is None :
                    return True
        return False

    def __search_in_dirction_w(self, i, j):
        """
        search win in diagonal /  dirction
        :param i: colon to start
        :param j: row to start
        :return: 1 if player 1 got win 2 if player 2 win else None
        """
        count_1 = 0
        count_2 = 0
        lst = []
        for k in range(min ( i,BOARD_LONG - j,4)):
            if self.__board[i - k][j+k] is not None:
                if self.__board[i - k][j+k]:
                    lst.append((i-k,j+k+1))
                    count_1 += 1
                else:
                    lst.append((i - k, j + k + 1))
                    count_2 += 1
                if count_1 > 3:
                    self.__winner_cord_lst = lst
                    return 1
                if count_2 > 3:
                    self.__winner_cord_lst = lst
                    return 2



    def get_winner(self):
        """

        :return: winner =(1,2) tiko=0 else None
        """
        for i in range(BOARD_WEDTH):
            for j in range(BOARD_LONG):
                if self.__board[i][j] is not None:
                    d = self.__search_in_dirction_d(i, j)
                    r = self.__search_in_dirction_r(i, j)
                    x = self.__search_in_dirction_x(i, j)
                    w = self.__search_in_dirction_w(i, j)
                    if w is not None:
                        return w
                    if x is not None:
                        return x
                    if r is not None:
                        return r
                    if d is not None:
                        return d
        if self.__check_tiko()is not True :
            return 0


    def get_player_at(self, row, col):
        """

        :param row:
        :param col:
        :return: the plyer in this cord else None
        """
        if row < 6 and row >= 0 :
            if col < 7 and col >= 0 :
                if self.__board[col][row] is None :
                    return None
                elif self.__board[col][row]:
                    return 1
                else:
                    return 2
        return "Illegal move"



    def get_current_player(self):
        """

        :return: the current turn of the  player
        """
        if self.get_winner() is not None:
            return
        if self.__turn > 0:
            return 1
        return 2

