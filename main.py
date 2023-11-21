from Player import  *
from Dice import *

playerName1 = str(input("Enter the name of the first player: "))
playerName2 = str(input("Enter the name of the second player: "))

player1 = Player(playerName1)
player2 = Player(playerName2)
Player.addPlayer(player1)
Player.addPlayer(player2)

while True:
    currentPlayer = input("Enter name of player to play\nTo show winner enter {s} \nClick on q to quite \n")
    diceFaces = Dice.play()
    if currentPlayer == playerName1 :
        print(player1.play(diceFaces))
    elif currentPlayer == playerName2 :
        print(player2.play(diceFaces))

    if currentPlayer == "s" :
        Player.showWinner()
    if currentPlayer == "q" :
        break

