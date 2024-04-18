from Game import Game
import math


    

circle=chr(9679)
space= " "
x=9
y=5
z=0
line={}
charnum=0
while charnum < x:
    line.update({str(charnum): space})
    charnum +=1
    
while z<y:
    line[str(math.floor(x/2))]=circle
    line[str(math.floor(x/2)-z)]=circle
    line[str(math.floor(x/2)+z)]= circle
    txt= ''
    for key in line.keys():
        txt+=line[key]
    print(space*4 + txt)
    z +=1



game = Game()
winNum=0 # the number of wins
for x in game._winList: # Detect the number from game list
    if game._winList[x]:
        winNum+=1

print("The final score of the game :")
if winNum >1:
    print(f"Congratulations!!\n You won {winNum} times.")
else:
    print(f"Good luck!!\n You lost {3 - winNum} times.")