import tkinter as tk
from .game import Game
from .ai import AI

BOARD_WEDTH = 1024
RIGHT_SHOLAIM_WEDTH =360
LEFT_SHOLAIM_WEDTH = 25
BOARD_LONG = 495
UP_SHOLAIM_WEDTH =0
DOWN_SHOLAIM_WEDTH =37
DISK_CENTER_X = 20
DISK_CENTER_Y = 27
BACKGROUND_FILE_NAME = "ex12//lo74.png"
WOOD_BACKGROUND_FILE_NAME = "ex12//5shbe33.png"
RED_DISK_FILE_NAME = "ex12//27jr2.png"
BLUE_DISK_FILE_NAME = "ex12//17jr1.png"
GAME_OVER = ""
WINNER_DISCK = ""

class Menu:
    """
    this class is the menu of the game and this class call the board and the board can
    call him again by clicking in the button return to menu
    """
    def __init__(self):
        """
        menu:the menu windo
        """
        self.menu = tk.Tk()


    def backgriund(self):
        """
        this func containe all the board consructer
        and apply thim
        :return:None
        """
        self.__background_frame()
        self.one_player_button()
        self.tow_player_button()
        self.__quit_button()
        self.menu.mainloop()


    def __background_frame(self):
        """
        the back ground frame
        :return:None
        """
        frame = tk.Frame(self.menu, width=886, height=600, bg="brown")
        frame.pack()


    def one_player_button(self):
        """

        :return:None
        """
        one_player = tk.Button(self.menu, text="One player vs Cup",\
                               command=self.one_player_chosed, font=("Helvetica", 20))
        one_player.place(x=330, y=200)

    def one_player_chosed(self):
        """
        here we call to the board
        :return:
        """
        self.menu.destroy()
        root = Board()
        root.comp = True
        root.build_board()


    def __quit_button(self):
        """
        quit the game
        :return:
        """
        quet = tk.Button(self.menu, text="    quit     ", command=self.menu.destroy, font=("Helvetica", 20))
        quet.place(x=385, y=300)


    def tow_player_button(self):
        """

        :return:
        """
        tow_player = tk.Button(self.menu, text="Tow players", command=self.tow_palyer_chose, font=("Helvetica", 20))
        tow_player.place(x=365,y=100)


    def tow_palyer_chose(self):
        """
            here we call to the board
            :return:
            """
        self.menu.destroy()
        root = Board()
        root.build_board()



class Board :
    """
    this is the main GUi of the game
    """
    def __init__(self):
        """
        define obj fields
        """
        self.board = tk.Tk()
        self.game = Game()
        self.still_dre = True
        self.game_end  = False
        self.comp = False #if hte option chose to play vs comp


    def build_board(self):
        """
        construct the board and loop it
        :return:
        """
        board = self.board
        self.__get_the_click_coords()
        self.__add_back_to_menu_button()
        self.__add_background()
        return board


    def __add_background(self):
        """
        build the board back ground
        :return:
        """
        background = tk.PhotoImage(file=BACKGROUND_FILE_NAME)
        label_img = tk.Label(self.board, image=background)
        label_img.place(x=0, y=0)
        background2 = tk.PhotoImage(file=WOOD_BACKGROUND_FILE_NAME)
        label_img = tk.Label(self.board, image=background2)
        label_img.place(x=702, y=50)
        background3 = tk.PhotoImage(file="ex12//blanka22.png")
        label_img = tk.Label(self.board, image=background3)
        label_img.place(x=655, y=497)
        background4 = tk.PhotoImage(file="ex12//blanka1.png")
        label_img = tk.Label(self.board, image=background4)
        label_img.place(x=570, y=497)
        background5 = tk.PhotoImage(file="ex12//blanka1.png")
        label_img = tk.Label(self.board, image=background5)
        label_img.place(x=480, y=497)
        background6 = tk.PhotoImage(file="ex12//blanka1.png")
        label_img = tk.Label(self.board, image=background6)
        label_img.place(x=390, y=497)
        background7 = tk.PhotoImage(file="ex12//blanka1.png")
        label_img = tk.Label(self.board, image=background7)
        label_img.place(x=296, y=497)
        background8 = tk.PhotoImage(file="ex12//blanka1.png")
        label_img = tk.Label(self.board, image=background8)
        label_img.place(x=206, y=497)
        background9 = tk.PhotoImage(file="ex12//blanka1.png")
        label_img = tk.Label(self.board, image=background9)
        label_img.place(x=115, y=497)
        background10 = tk.PhotoImage(file="ex12//blanka22.png")
        label_img = tk.Label(self.board, image=background10)
        label_img.place(x=0, y=497)
        self.board.mainloop()


    def __add_back_to_menu_button(self):
        """
        add back to menu button
        :return:
        """
        back_to_menu = tk.Button(self.board, text="back to menu", command=self.back_to_menu_chosed, font=("Helvetica", 20))
        back_to_menu.place(x=700, y=0)


    def back_to_menu_chosed(self):
        """
        back to menu
        :return:
        """
        self.board.destroy()
        game_menu = Menu()
        game_menu.backgriund()


    def __check_colon(self,coord):
        """
        this func return if the click is legal or not
        :param coord: click ccord
        :return:
        """
        s = self.__convert_cord_to_colon(coord)
        board = self.game.board()
        for j in range(6):
            if board[s][5-j] is None:
                return True
        return False


    def __clicked(self,event):
        """
        call another func after check if evrey thing is legal
        :param event: click cord
        :return:
        """
        coord = (event.x,event.y)
        if self.still_dre and self.__check_colon(coord) :
            self.__add_disckes(coord)


    def __get_the_click_coords(self):
        """
        here we get the click coord
        :return:
        """
        frame = tk.Frame(self.board,width=886, height=600, bg="brown")
        frame.bind("<Button-1>", self.__clicked)
        frame.pack()


    def __add_red_disck(self,cord):
        """
        this func add red disck
        :param the ord of the click in the board game
        :return:
        """
        turn_lable = tk.Label(self.board, width=300, height=100, bg="black")
        turn_lable.place(x=700,y=55)
        coord = self.__convert_colon_to_cord(cord)
        red_disck = tk.PhotoImage(file=RED_DISK_FILE_NAME)
        label_img = tk.Label(self.board, image=red_disck)
        label_img.place(x=coord[0], y=coord[1])
        if self.game_end:
            if self.game.get_winner()!= 0 :
                self.__winner_aplly()
            else:
                self.__tiko_aply()
        self.board.mainloop()


    def __tiko_aply(self):
        """
        tiko label
        :return:
        """
        lable_txt = tk.Label(self.board, text="ROUND DRAW" , font=("Helvetica", 20))
        lable_txt.place(x=300, y=0)


    def __add_blue_disch(self,cord):
        """
        this func add black disck
        :param the ord of the click in the board game
        :return:
        """
        turn_lable = tk.Label(self.board, width=300, height=100, bg="red")
        turn_lable.place(x=700, y=55)
        coord = self.__convert_colon_to_cord(cord)
        blue_disck = tk.PhotoImage(file=BLUE_DISK_FILE_NAME)
        label_img = tk.Label(self.board, image=blue_disck)
        label_img.place(x=coord[0], y=coord[1])
        if self.game_end :
            self.__winner_aplly()
        self.board.mainloop()


    def __add_disckes(self,coord):
        """

        :param coord: click coord
        :return:
        """
        colon = self.__convert_cord_to_colon(coord)
        self.game.make_move(colon)
        cord = self.game.colon_row_player[0]
        if self.game.get_winner() is not None :
        #if its 2 players
            self.still_dre = False
            self.game_end = True
        if self.comp is not True:
            if self.game.colon_row_player[1] == 1:
                self.__add_blue_disch(cord)
            else:
                self.__add_red_disck(cord)
        else:
        #if its com player
            coord = self.__convert_colon_to_cord(cord)
            blue_disck = tk.PhotoImage(file=BLUE_DISK_FILE_NAME)
            label_img = tk.Label(self.board, image=blue_disck)
            label_img.place(x=coord[0], y=coord[1])
            if self.game_end:
                self.__winner_aplly()
                self.board.mainloop()
                return
            comp_ai = AI(self.game,2)
            comp_ai.board = self.game.board
            ai_cord = comp_ai.find_legal_move()
            self.game.make_move(ai_cord)
            cord_ai = self.game.colon_row_player[0]
            coord = self.__convert_colon_to_cord(cord_ai)
            red_disck = tk.PhotoImage(file=RED_DISK_FILE_NAME)
            label_img = tk.Label(self.board, image=red_disck)
            label_img.place(x=coord[0], y=coord[1])
            if self.game.get_winner() is not None:
                self.still_dre = False
                self.game_end = True
            if self.game_end and self.game.get_winner():
                self.__winner_aplly()
            elif self.game_end :
                self.__tiko_aply()
            self.board.mainloop()


    def __get_row_first_none_cord(self,colon):
        """

        :param colon: volon
        :return: row
        """
        for i in range(6):
            if self.game.get_player_at(6-i,colon) is None :
                return 6-i


    def __winner_aplly(self):
        """
        aplly winner
        :return:
        """
        game_over = tk.PhotoImage(file=GAME_OVER)
        label_img = tk.Label(self.board, image=game_over)
        label_img.place(x=0, y=0)
        winner = self.game.get_winner()
        lable_txt = tk.Label(self.board, text="Player "+str(winner) + " Is WINNER",font=("Helvetica", 20))
        lable_txt.place(x=300,y=0)
        # remark the winner discks
        lst = self.game.get_winner_cord_lst()
        coord = self.__convert_colon_to_cord(lst[0])
        label_img = tk.Label(self.board, text="V",font=("Helvetica", 20))
        label_img.place(x=coord[0], y=coord[1])
        coord = self.__convert_colon_to_cord(lst[1])
        label_img = tk.Label(self.board, text="V",font=("Helvetica", 20))
        label_img.place(x=coord[0], y=coord[1])
        coord = self.__convert_colon_to_cord(lst[2])
        label_img = tk.Label(self.board, text="V",font=("Helvetica", 20))
        label_img.place(x=coord[0], y=coord[1])
        coord = self.__convert_colon_to_cord(lst[3])
        label_img = tk.Label(self.board, text="V",font=("Helvetica", 20))
        label_img.place(x=coord[0], y=coord[1])


    def __convert_colon_to_cord(self,colon_row):
        """
        convert from game cord to board cord
        :param colon_row: tupple of the cord of the game
        :return:
        """
        colon_width = (BOARD_WEDTH - LEFT_SHOLAIM_WEDTH - RIGHT_SHOLAIM_WEDTH) // 7
        row_wedth = (BOARD_LONG - UP_SHOLAIM_WEDTH - DOWN_SHOLAIM_WEDTH) // 6
        x = colon_row[0] * colon_width + DISK_CENTER_X + LEFT_SHOLAIM_WEDTH
        y = colon_row[1] * row_wedth + DISK_CENTER_Y -67
        return (x,y)


    def __convert_cord_to_colon(self,cord):
        """
        convert from click cord to colon
        :param cord: click cord
        :return:
        """
        colon_width = (BOARD_WEDTH-LEFT_SHOLAIM_WEDTH-RIGHT_SHOLAIM_WEDTH)//7
        colon = (cord[0]-LEFT_SHOLAIM_WEDTH)//colon_width
        return colon
