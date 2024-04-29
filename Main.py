from Game import Game
import math


game = Game()
winNum=0 # the number of wins
for x in game._winList: # Detect the number from game list
    if game._winList[x]:
        winNum+=1

print("The final score of the game :")
if winNum >1:
    print(f"Congratulations!!\nYou won {winNum} times.")
else:
    print(f"Good luck!!\n You lost {3 - winNum} times.")