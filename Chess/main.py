import copy
class Player:
    firstOrSecond = -1
    name = ""
    P1 = False
    P2 = False
    def __init__(self, name, firstOrSecond):
        self.firstOrSecond = firstOrSecond
        if(firstOrSecond==1):
            self.P1 = True
        if(firstOrSecond==2):
            self.P2 = True
        self.name = name
class Empty:
    player = None
    locationR = -1
    locationC = -1
    def __init__(self, locR, locC):
        self.locationR=locR
        self.locationC=locC
    def getPieceName(self):
        return "Empty "
class Rook:
    player = None
    locationR = -1
    locationC = -1
    def __init__(self, player1 ,locR, locC):
        self.locationR = locR
        self.locationC = locC
        self.player = player1
    def getPieceName(self):
        return "Rook  "
    def Availablemoves(self, board):
        listOfLocations = []
        r = self.locationR
        c = self.locationC
        while True:
            '''down'''
            if((r+1>=0 and r+1<=7) and (type(board.board[r+1][c])==Rook or type(board.board[r+1][c])==Knight or type(board.board[r+1][c])==Bishop or type(board.board[r+1][c])==Queen or type(board.board[r+1][c])==King or type(board.board[r+1][c])==Pawn)):
                listOfLocations.append([r+1,c])
                break
            elif (r+1>=0 and r+1<=7):
                r+=1
                listOfLocations.append([r,c])
            else:
                break
        r = self.locationR
        c = self.locationC
        while True:
            '''right'''
            if((c+1>=0 and c+1<=7) and (type(board.board[r][c+1])==Rook or type(board.board[r][c+1])==Knight or type(board.board[r][c+1])==Bishop or type(board.board[r][c+1])==Queen or type(board.board[r][c+1])==King or type(board.board[r][c+1])==Pawn)):
                listOfLocations.append([r,c+1])
                break
            elif(c+1>=0 and c+1<=7):
                c+=1
                listOfLocations.append([r,c])
            else:
                break
        r = self.locationR
        c = self.locationC
        while True:
            '''up'''
            if((r-1>=0 and r-1<=7) and (type(board.board[r-1][c])==Rook or type(board.board[r-1][c])==Knight or type(board.board[r-1][c])==Bishop or type(board.board[r-1][c])==Queen or type(board.board[r-1][c])==King or type(board.board[r-1][c])==Pawn)):
                listOfLocations.append([r-1,c])
                break
            elif(r-1>=0 and r-1<=7):
                r-=1
                listOfLocations.append([r,c])
            else:
                break
        r = self.locationR
        c = self.locationC
        while True:
            '''left'''
            if((c-1>=0 and c-1<=7) and (type(board.board[r][c-1])==Rook or type(board.board[r][c-1])==Knight or type(board.board[r][c-1])==Bishop or type(board.board[r][c-1])==Queen or type(board.board[r][c-1])==King or type(board.board[r][c-1])==Pawn)):
                listOfLocations.append([r,c-1])
                break
            elif((c-1>=0 and c-1<=7)):
                c-=1
                listOfLocations.append([r,c])
            else:
                break
        return listOfLocations
class Knight:
    player = None
    locationR = -1
    locationC = -1
    def __init__(self, player1 ,locR, locC):
        self.locationR = locR
        self.locationC = locC
        self.player = player1
    def getPieceName(self):
        return "Knight"
    def Availablemoves(self, board):
        listOfLocations = []
        r = self.locationR
        c = self.locationC
        '''upright'''
        if((r-2>=0 and r-2<=7) and (c+1>=0 and c+1<=7)):
            if(type(board.board[r-2][c+1])==Empty):
                r-=2
                c+=1
                listOfLocations.append([r,c])
            else:
                listOfLocations.append([r - 2, c + 1])
        r = self.locationR
        c = self.locationC
        '''upleft'''
        if ((r - 2 >= 0 and r - 2 <= 7) and (c - 1 >= 0 and c - 1 <= 7)):
            if (type(board.board[r - 2][c - 1]) == Empty):
                r -= 2;
                c -= 1;
                listOfLocations.append([r, c])
            else:
                listOfLocations.append([r - 2, c - 1])
        r = self.locationR
        c = self.locationC
        '''righttop'''
        if ((r - 1 >= 0 and r - 1 <= 7) and (c + 2 >= 0 and c + 2 <= 7)):
            if (type(board.board[r - 1][c + 2]) == Empty):
                r -= 1;
                c += 2;
                listOfLocations.append([r, c])
            else:
                listOfLocations.append([r - 1, c + 2])

        r = self.locationR
        c = self.locationC
        '''rightbottom'''
        if ((r + 1 >= 0 and r + 1 <= 7) and (c + 2 >= 0 and c + 2 <= 7)):
            if (type(board.board[r + 1][c + 2]) == Empty):
                r += 1
                c += 2
                listOfLocations.append([r, c])
            else:
                listOfLocations.append([r + 1, c + 2])
        r = self.locationR
        c = self.locationC
        """lefttop"""
        if ((r - 1 >= 0 and r - 1 <= 7) and (c - 2 >= 0 and c - 2 <= 7)):
            if (type(board.board[r - 1][c - 2]) == Empty):
                r -= 1
                c -= 2
                listOfLocations.append([r, c])
            else:
                listOfLocations.append([r - 1, c - 2])

        r = self.locationR
        c = self.locationC
        '''leftbottom'''
        if ((r + 1 >= 0 and r + 1 <= 7) and (c - 2 >= 0 and c - 2 <= 7)):
            if (type(board.board[r + 1][c - 2]) == Empty):
                r += 1
                c -= 2
                listOfLocations.append([r, c])
            else:
                listOfLocations.append([r + 1, c - 2])

        r = self.locationR
        c = self.locationC
        '''bottomleft'''
        if ((r + 2 >= 0 and r + 2 <= 7) and (c - 1 >= 0 and c - 1 <= 7)):
            if (type(board.board[r + 2][c - 1]) == Empty):
                r += 2
                c -= 1
                listOfLocations.append([r, c])
            else:
                listOfLocations.append([r + 2, c - 1])
        r = self.locationR
        c = self.locationC
        '''bottomright'''
        if ((r + 2 >= 0 and r + 2 <= 7) and (c + 1 >= 0 and c + 1 <= 7)):
            if (type(board.board[r + 2][c + 1]) == Empty):
                r += 2
                c += 1
                listOfLocations.append([r, c])
            else:
                listOfLocations.append([r + 2, c + 1])
        return listOfLocations
class Bishop:
    player = None
    locationR = -1
    locationC = -1
    def __init__(self, player1 ,locR, locC):
        self.locationR = locR
        self.locationC = locC
        self.player = player1
    def getPieceName(self):
        return "Bishop"
    def Availablemoves(self, board):
        availableMoves = []
        '''daigtopright'''
        r=self.locationR;
        c=self.locationC;
        while (True):
            if(((r - 1 >= 0 and r - 1 <= 7) and (c + 1 >= 0 and c + 1 <= 7)) and (type(board.board[r-1][c+1])==Empty)):
                r-=1
                c+=1
                availableMoves.append([r,c])
            else:
                break;

        '''diagtopleft'''
        r = self.locationR;
        c = self.locationC;
        while (True):
            if (((r - 1 >= 0 and r - 1 <= 7) and (c - 1 >= 0 and c - 1 <= 7)) and (type(board.board[r - 1][c - 1]) == Empty)):
                r -= 1
                c -= 1
                availableMoves.append([r, c])
            else:
                break;
        '''diagbottomleft'''
        r = self.locationR;
        c = self.locationC;
        while (True):
            if (((r + 1 >= 0 and r + 1 <= 7) and (c - 1 >= 0 and c - 1 <= 7)) and (type(board.board[r + 1][c - 1]) == Empty)):
                r += 1
                c -= 1
                availableMoves.append([r, c])
            else:
                break

        '''diagbottomright'''
        r = self.locationR;
        c = self.locationC;
        while (True):
            if (((r + 1 >= 0 and r + 1 <= 7) and (c + 1 >= 0 and c + 1 <= 7)) and (
                    type(board.board[r + 1][c + 1]) == Empty)):
                r += 1
                c += 1
                availableMoves.append([r, c])
            else:
                break;
        return availableMoves;
class Queen:
    player = None
    locationR = -1
    locationC = -1
    def __init__(self, player1 ,locR, locC):
        self.locationR = locR
        self.locationC = locC
        self.player = player1
    def getPieceName(self):
        return "Queen "
    def Availablemoves(self, board):
        availableMoves = []
        '''daigtopright'''
        r = self.locationR;
        c = self.locationC;
        while (True):
            if (((r - 1 >= 0 and r - 1 <= 7) and (c + 1 >= 0 and c + 1 <= 7)) and (
                    type(board.board[r - 1][c + 1]) == Empty)):
                r -= 1
                c += 1
                availableMoves.append([r, c])
            else:
                break;

        '''diagtopleft'''
        r = self.locationR;
        c = self.locationC;
        while (True):
            if (((r - 1 >= 0 and r - 1 <= 7) and (c - 1 >= 0 and c - 1 <= 7)) and (
                    type(board.board[r - 1][c - 1]) == Empty)):
                r -= 1
                c -= 1
                availableMoves.append([r, c])
            else:
                break;
        '''diagbottomleft'''
        r = self.locationR;
        c = self.locationC;
        while (True):
            if (((r + 1 >= 0 and r + 1 <= 7) and (c - 1 >= 0 and c - 1 <= 7)) and (
                    type(board.board[r + 1][c - 1]) == Empty)):
                r += 1
                c -= 1
                availableMoves.append([r, c])
            else:
                break

        '''diagbottomright'''
        r = self.locationR;
        c = self.locationC;
        while (True):
            if (((r + 1 >= 0 and r + 1 <= 7) and (c + 1 >= 0 and c + 1 <= 7)) and (
                    type(board.board[r + 1][c + 1]) == Empty)):
                r += 1
                c += 1
                availableMoves.append([r, c])
            else:
                break;
        while True:
            '''down'''
            if((r+1>=0 and r+1<=7) and (type(board.board[r+1][c])==Rook or type(board.board[r+1][c])==Knight or type(board.board[r+1][c])==Bishop or type(board.board[r+1][c])==Queen or type(board.board[r+1][c])==King or type(board.board[r+1][c])==Pawn)):
                break
            elif (r+1>=0 and r+1<=7):
                r+=1
                availableMoves.append([r,c])
            else:
                break
        r = self.locationR
        c = self.locationC
        while True:
            '''right'''
            if((c+1>=0 and c+1<=7) and (type(board.board[r][c+1])==Rook or type(board.board[r][c+1])==Knight or type(board.board[r][c+1])==Bishop or type(board.board[r][c+1])==Queen or type(board.board[r][c+1])==King or type(board.board[r][c+1])==Pawn)):
                break
            elif(c+1>=0 and c+1<=7):
                c+=1
                availableMoves.append([r,c])
            else:
                break
        r = self.locationR
        c = self.locationC
        while True:
            '''up'''
            if((r-1>=0 and r-1<=7) and (type(board.board[r-1][c])==Rook or type(board.board[r-1][c])==Knight or type(board.board[r-1][c])==Bishop or type(board.board[r-1][c])==Queen or type(board.board[r-1][c])==King or type(board.board[r-1][c])==Pawn)):
                break
            elif(r-1>=0 and r-1<=7):
                r-=1
                availableMoves.append([r,c])
            else:
                break
        r = self.locationR
        c = self.locationC
        while True:
            '''left'''
            if((c-1>=0 and c-1<=7) and (type(board.board[r][c-1])==Rook or type(board.board[r][c-1])==Knight or type(board.board[r][c-1])==Bishop or type(board.board[r][c-1])==Queen or type(board.board[r][c-1])==King or type(board.board[r][c-1])==Pawn)):
                break
            elif((c-1>=0 and c-1<=7)):
                c-=1
                availableMoves.append([r,c])
            else:
                break
        return availableMoves;

class King:
    player = None
    locationR = -1
    locationC = -1
    def __init__(self, player1 ,locR, locC):
        self.locationR = locR
        self.locationC = locC
        self.player = player1
    def getPieceName(self):
        return "King  "
    def Availablemoves(self, board):
        moves=[]
        r=self.locationR
        c=self.locationC
        if((c-1>=0 and c-1<=7) and (type(board.board[r][c-1])==Empty)):
            moves.append([r,c-1])
        if ((c + 1 >= 0 and c + 1 <= 7) and (type(board.board[r][c+1])==Empty)):
            moves.append([r, c + 1])
        if ((r - 1 >= 0 and r - 1 <= 7) and (type(board.board[r-1][c])==Empty)):
            moves.append([r - 1, c])
        if ((r + 1 >= 0 and r + 1 <= 7) and (type(board.board[r+1][c])==Empty)):
            moves.append([r + 1, c])
        return moves
class Pawn:
    player = None
    locationR = -1
    locationC = -1
    def __init__(self, player1 ,locR, locC):
        self.locationR = locR
        self.locationC = locC
        self.player = player1
    def getPieceName(self):
        return "Pawn  "
    def Availablemoves(self, board):
        r=self.locationR
        c=self.locationC
        moves=[]
        if(self.player.P1==True):
            if((r + 1 >= 0 and r + 1 <= 7) and type(board.board[r+1][c])==Empty):
                    moves.append([r+1,c])
        if(self.player.P1 == True):
            if ((r + 2 >= 0 and r + 2 <= 7) and type(board.board[r + 2][c]) == Empty):
                moves.append([r + 2,c])
        if(self.player.P2 == True):
            if ((r - 1 >= 0 and r - 1 <= 7) and type(board.board[r - 1][c]) == Empty):
                    moves.append([r - 1,c])
        if(self.player.P2 == True):
            if ((r - 2 >= 0 and r - 2 <= 7) and type(board.board[r - 2][c]) == Empty):
                    moves.append([r - 2,c])
        return moves


class Board:
    player1=None
    player2=None
    board = []
    def __init__(self,player11, player22):
        self.player1=player11
        self.player2=player22
    for r1 in range(0, 8):
        row = [Empty(r1,0),Empty(r1,1),Empty(r1,2),Empty(r1,3),Empty(r1,4),Empty(r1,5),Empty(r1,6),Empty(r1,7)]
        board.insert(r1,row)
    def fillBoardDefault(self):
        for r in range(0,8):
            for c in range(0,8):
                if(r==0):
                    if (c == 0 or c == 7):
                        self.board[r][c] = Rook(self.player1,r,c)
                    if (c == 1 or c == 6):
                        self.board[r][c] = Knight(self.player1,r,c)
                    if (c == 2 or c == 5):
                        self.board[r][c] = Bishop(self.player1,r,c)
                    if (c == 3):
                        self.board[r][c] = Queen(self.player1,r,c)
                    if (c == 4):
                        self.board[r][c] = King(self.player1,r,c)
                if(r==1):
                    self.board[r][c] = Pawn(self.player1,r,c)
                if(r==6):
                    self.board[r][c] = Pawn(self.player2,r,c)
                if(r==7):
                    if (c == 0 or c == 7):
                        self.board[r][c] = Rook(self.player2,r,c)
                    if (c == 1 or c == 6):
                        self.board[r][c] = Knight(self.player2,r,c)
                    if (c == 2 or c == 5):
                        self.board[r][c] = Bishop(self.player2,r,c)
                    if (c == 3):
                        self.board[r][c] = Queen(self.player2,r,c)
                    if (c == 4):
                        self.board[r][c] = King(self.player2,r,c)
    def checkForAvailableSpace(self,locR,LocC):
        if(self.board[locR][LocC].getPieceName()=="Empty "):
            return True
        else:
            return False
    def movePiece(self, oriLocR,oriLocC , FinalLocR, FinalLocC):
        if(self.checkForAvailableSpace(FinalLocR,FinalLocC)):
            CopyOri = copy.deepcopy(self.board[oriLocR][oriLocC])
            CopyFinal = copy.deepcopy(self.board[FinalLocR][FinalLocC])

            self.board[FinalLocR][FinalLocC] = self.board[oriLocR][oriLocC]

            self.board[FinalLocR][FinalLocC].locationR = FinalLocR
            self.board[FinalLocR][FinalLocC].locationC = FinalLocC

            self.board[oriLocR][oriLocC] = Empty(oriLocR, oriLocC)
            return True
        else:
            return False
    def printBoard(self):
        StringBoard = []
        for r in range (0,8):
            row = ["","","","","","","",""]
            for c in range (0,8):
                    if(self.board[r][c].player!=None):
                        row[c] = self.board[r][c].getPieceName()+"P"+str(self.board[r][c].player.name)
                    else:
                        row[c] = self.board[r][c].getPieceName() + "PN"
            StringBoard.append(row)
        for r1 in range(0,8):
            print(StringBoard[r1])


def main():
    p1 = Player("1",1)
    p2 = Player("2",2)
    board = Board(p1,p2)
    board.fillBoardDefault()
    board.printBoard()
    print("\n\n\n\n\n")
    board.movePiece(0,0,2,3)
    board.printBoard();
    print(board.board[2][3].getPieceName()+"P"+str(board.board[2][3].player.name),": ",board.board[2][3].Availablemoves(board))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
