import os
import random as r

gridgame = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
plays = 0
playernow = 0
winner = 0
maxmoves = 9
def drawDisplay():
    print("     0   1   2")
    for i in range(0, 3):        
        print(f"{i}    {gridgame[i][0]} | {gridgame[i][1]} | {gridgame[i][2]}")
        if i < 2:
            print("    -----------")
    print(f"Jogadas: {plays}")

def playGame():
    global playernow
    global plays
    if playernow == 0:
        if plays == maxmoves:
            os.system("cls")
            print("Empate")
            os.system("pause")
            askNewGame()
        try:
            c = int(input("Digite o numero da coluna: "))
            l = int(input("Digite o numero da linha: "))
        except:
            print("Digite somente numeros.")
            playGame()
        if c > 3 or c < 0 or l < 0 and l > 3:
            print("Numeros invalidos.")
            playGame()
        if gridgame[l][c] == " ":
            gridgame[l][c] = "X"
            os.system("cls")
            drawDisplay()
            playernow = 1
            plays += 1
        if checkWinner("X") == True:
            os.system("cls")
            print("O jogador X ganhou")
            os.system("pause")
            askNewGame()
        playGame()
    if playernow == 1:
        if plays == maxmoves:
            os.system("cls")
            print("Empate")
            os.system("pause")
            askNewGame()
        c = r.randint(0, 2)
        l = r.randint(0, 2)
        if gridgame[l][c] == " ":
            gridgame[l][c] = "O"
            playernow = 0
            plays += 1
            if checkWinner("O") == True:
                os.system("cls")
                print("O ganhou")
                os.system("pause")
                askNewGame()
            drawDisplay()
            playGame()
            
        else:
            playGame()

def checkWinner(playtime):
    for n in range(0, 3):
        if gridgame[n][0] == playtime and gridgame[n][1] == playtime and gridgame[n][2] == playtime:
            return True
        if gridgame[0][n] == playtime and gridgame[1][n] == playtime and gridgame[2][n] == playtime:
            return True
    if gridgame[0][0] == playtime and gridgame[1][1] == playtime and gridgame[2][2] == playtime:
        return True
    elif gridgame[0][2] == playtime and gridgame[1][1] == playtime and gridgame[2][0] == playtime:
        return True
    
def askNewGame():
    global gridgame
    global playernow
    global plays
    os.system("cls")
    ask = input("Deseja jogar novamente?[s/n]: ").strip()[0]
    if ask.lower() == "s":
        gridgame = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        os.system("cls")
        drawDisplay()
        plays = 0
        playernow = 0
        playGame()
    elif ask.lower() == "n":
        exit()

drawDisplay()
playGame()