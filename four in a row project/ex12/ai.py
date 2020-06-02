import copy
import random
import collections
BOARD_LONG = 6
BOARD_WEDTH = 7
class AI:
    """
    comp player
    """
    def __init__(self, game, player):
        """

        :param game: Game()
        :param player: comp player
        """
        self.playir = player
        self.obset_player = self.__obst_player()
        self.game = game
        self.air_board = self.__fill_board()
        self.board = self.air_board
        self.turn = -1


    def __obst_player(self):
        """

        :return: obset_player
        """
        if self.playir is 1:
            return 2
        else:
            return 1


    def __search_in_dirction_dd(self,i,j):
        """
        search win in down  dirction
        :param i: colon to start
        :param j: row to start
        :return: 1 if player 1 got win 2 if player 2 win else None
                """
        count_1 = 0
        count_2 = 0
        for k in range(min(BOARD_LONG-j,4)):
            if self.board[i][j+k]==1 :
                count_1 +=1
            else:
                count_2 +=1
            if count_1 >3 :
                return 1
            if count_2 >3:
                return 2


    def __search_in_dirction_rr(self, i, j):
        """
        search win in right  dirction
        :param i: colon to start
        :param j: row to start
        :return: 1 if player 1 got win 2 if player 2 win else None
        """
        count_1 = 0
        count_2 = 0
        for k in range(min(BOARD_WEDTH - i,4)):
            if self.board[i+k][j] is not None:
                if self.board[i+k][j]==1:
                    count_1 += 1
                else:
                    count_2 += 1
                if count_1 > 3:
                    return 1
                if count_2 > 3:
                    return 2


    def __search_in_dirction_xx(self, i, j):
        """
        search win in diagonal /  dirction
        :param i: colon to start
        :param j: row to start
        :return: 1 if player 1 got win 2 if player 2 win else None
        """
        count_1 = 0
        count_2 = 0
        for k in range(min (BOARD_WEDTH - i,BOARD_LONG - j,4)):
            if self.board[i + k][j+k] is not None:
                if self.board[i + k][j+k]==1:
                    count_1 += 1
                else:
                    count_2 += 1
                if count_1 > 3:
                    return 1
                if count_2 > 3:
                    return 2


    def __search_in_dirction_ww(self, i, j):
        """
        search win in diagonal \  dirction
        :param i: colon to start
        :param j: row to start
        :return: 1 if player 1 got win 2 if player 2 win else None
        """
        count_1 = 0
        count_2 = 0
        for k in range(min ( i,BOARD_LONG - j,4)):
            if self.board[i - k][j+k] is not None:
                if self.board[i - k][j+k]==1:
                    count_1 += 1
                else:
                    count_2 += 1
                if count_1 > 3:
                    return 1
                if count_2 > 3:
                    return 2


    def __get_winner(self):
        """

        :return: winner
        """
        for i in range(BOARD_WEDTH):
            for j in range(BOARD_LONG):
                if self.board[i][j] is not None:
                    d = self.__search_in_dirction_dd(i, j)
                    r = self.__search_in_dirction_rr(i, j)
                    x = self.__search_in_dirction_xx(i, j)
                    w = self.__search_in_dirction_ww(i, j)
                    if w is not None:
                        return w
                    if x is not None:
                        return x
                    if r is not None:
                        return r
                    if d is not None:
                        return d

    def check_colon(self,s):
        """

        :param s: colon
        :return: if its llegal
        """
        board = copy.deepcopy(self.board)
        for j in range(6):
            if board[s][5-j] is None:
                return False
        return True


    def add_cord_to_col(self,i,player):
        """

        :param i: colon
        :param player: player(1,2)
        :return: chek if colon good for the player
        """
        board = copy.deepcopy(self.air_board)
        self.board = board
        for j in range(BOARD_LONG):
            if board[i][BOARD_LONG-j-1] is None:
                board[i][BOARD_LONG-1-j] = player
                self.board = board
                if self.__get_winner() == player:
                    return True
                else:
                    return False
        return False


    def __new_day(self):
        """

        :return: return the most good colon and legal as posipol
        """
        self.air_board = self.__fill_board()
        for i in range(BOARD_WEDTH):
            if self.add_cord_to_col(i,self.playir):
                return i
        for k in range(BOARD_WEDTH):
            if self.add_cord_to_col(k,self.obset_player):
                return k
        still_dre = True
        while still_dre:
            s = random.randint(0,BOARD_WEDTH-1)
            still_dre = self.check_colon(s)
        return s


    def __fill_board(self):
        """
        build the board dlist
        :return: lst of the board
        """
        lst = []
        for i in range(BOARD_WEDTH):
            lst.append([])
            for j in range(BOARD_LONG):
                lst[i].append(self.game.get_player_at(j,i))
        return lst


    def find_legal_move(self, timeout=None):
        """

        :param timeout:
        :return: return the most good colon and legal as posipol
        """
        return self.__new_day()


    def get_last_found_move(self):
        pass




