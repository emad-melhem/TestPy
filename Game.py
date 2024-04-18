import random
from Hand import Hand

class Game:
    _gameRound=1
    _contenueGame=True # To detect if the user wants to continue the game
    _winList={"1":False, "2":False, "3":False}
    
    def __init__(self):
        self.start()

    def start(self): # start the game
        try:
            while self._gameRound <4 and self._contenueGame:
                print(f"This is round : {self._gameRound}")
                self.startRound()
                self._gameRound +=1
                if self._gameRound <4:   #check if continue the game
                    x= input("Do you want to continue? (Y/N)")
                    if x.lower()=="n":
                        self._contenueGame=False
        except Exception as error:
            print(error)

    def startRound(self): # start the round
        x= input("Select Rock (0), Paper (1), or Scissors (2) !")
        if int(x)>= 0 and int(x) <=2: # Detect the select number from user
            hand= Hand(int(x))
            compid= random.randrange(0,3) #random the selected id from computer
            y = hand.isPowerfullThan(compid)
            if y==0:
                print("The result is draw !")
                self.startRound()  # repeat the round if it is draw
            else:
                isWin= y >0
                computerHand= Hand(compid)
                self._winList[str(self._gameRound)] = isWin # Set the result in winList
                print(f"You are select {hand.handName()}")
                print(f"Computer is select {computerHand.handName()}")
                if isWin:
                    print("You won ! Congrats")
                else:
                    print("You lost ! good luck")
                
        else:
            raise Exception("Sorry, number is out of rang !!") # raise an excption if the user selected number out of range 
        





