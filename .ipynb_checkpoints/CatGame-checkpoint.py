from tkinter import *
from tkinter import messagebox

class Cat:
    def __init__(self):
        self.current_player = "O"
        self.board = [["" for _ in range(3)] for _ in range(3)]

    def switch_player(self): 
        self.current_player = "X" if self.current_player == "O" else "O"

    def make_move(self, x, y):
        if self.board[x][y] == "":
            self.board[x][y] = self.current_player
            return True
        return False

    def check_winner(self):
        # Verificar filas y columnas
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
               all(self.board[j][i] == self.current_player for j in range(3)):
                return True

        # Verificar diagonales
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            return True

        return False

    def reset_game(self):
        self.current_player = "O"
        self.board = [["" for _ in range(3)] for _ in range(3)]


class Board:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Gato")
        
        self.cat_game = Cat()  # Instancia de la clase lógica Cat
        self.buttons = [[Button(self.root, text="", width=10, height=5, 
                                command=lambda x=i, y=j: self.handle_click(x, y))
                         for j in range(3)] for i in range(3)]


        # Colocar botones en la cuadrícula
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

    def handle_click(self, x, y):
        if self.cat_game.make_move(x, y):
            self.buttons[x][y].config(text=self.cat_game.current_player)

            if self.cat_game.check_winner():
                messagebox.showinfo("Juego terminado", f"¡Jugador {self.cat_game.current_player} ha ganado!")
                self.reset_game()
            elif all(self.buttons[i][j]['text'] != "" for i in range(3) for j in range(3)):
                messagebox.showinfo("Juego terminado", "¡Es un empate!")
                self.reset_game()
            else:
                self.cat_game.switch_player()

    def reset_game(self):
        self.cat_game.reset_game()
        for row in self.buttons:
            for button in row:
                button.config(text="", state="normal")


if __name__ == "__main__":
    root = Tk()
    board = Board(root)
    root.mainloop()