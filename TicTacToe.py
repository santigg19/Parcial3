class TaTeTi():

    #board = [(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')]
    
    
    def __init__(self, table = None):

        if not table:
            self.board = [' ' for _ in range(9)]    # Lo del test

        else:
            self.board = table

            
    # Verifica si el tablero esta lleno o no
    def full(self):

        return " "  not in self.board


    # Verifica cada escenario posible de victoria, caso contrario, devuelve False. No es lo mas estetico pero funciona
    def win(self):


        if self.board[0] == self.board[3] and self.board[0] == self.board[6] and self.board[3] != " ":
            return True

        elif self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[4] != " ":
            return True

        elif self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[8] != " ":
            return True

        elif self.board[6] == self.board[7] and self.board[6] == self.board[8] and self.board[8] != " ":
            return True
        
        elif self.board[3] == self.board[4] and self.board[3] == self.board[5] and self.board[5] != " ":
            return True
        
        elif self.board[0] == self.board[1] and self.board[0] == self.board[2] and self.board[2] != " ":
            return True
        
        elif self.board[0] == self.board[4] and self.board[0] == self.board[8] and self.board[8] != " ":
            return True

        elif self.board[2] == self.board[4] and self.board[2] == self.board[6] and self.board[6] != " ":
            return True

        else:
            return False


    def validate(self, position):

        return self.board[position - 1] == " "
        #return self.board(position - 1) == " "
        

    # Asigna los  valores si estos son validos
    def assign(self, position, number):

        if self.validate(position):
            self.board[position - 1] = number

        else:
            raise Exception

    #def draw_board(self, board, display):
        #pass


    def draw_board(self):

        self.display = "\n"

        for i in range(9):

            if self.board[i] != " ":                # Si es distinto de vacio en el tablero en i, muestra el valor
                self.display += " " + self.board[i] + " "

            else:
                self.display += " " + str(1 + i) + " "

            if i == 2 or i == 5:
                self.display += "\n---+---+---\n"   # Separacion entre filas

            elif i == 8:
                self.display += "\n"                # Como es el ultimo lo separa

            else:
                self.display += "|"                 # Separacion entre columnas
            
        return self.display





