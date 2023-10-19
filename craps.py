import random
'''
Pass Line
An even money bet, made on the first roll of the dice (known as the “come out roll”). 
You win if a 7 or 11 roll, or lose if 2, 3, or 12 roll (known as “craps”). 
Any other number that rolls becomes the “point” and the point must roll again before a 7 to win.

Don't Pass Line
An even money bet, which is the opposite of the pass line. 
You lose on the “come out” roll if the shooter rolls a 7 or 11. 
You win on a 2 or 3 (12 is a tie). 
Once a point is established, you lose if the point is thrown and win if a 7 rolls.'''

class game:
    def __init__(self) -> None:
        self.bets()
        #self.roll()
        self.play()
    def bets(self):
        bet = input("Enter what bet you will do, The options are: Pass line, Dont pass line or No bet: ").lower()
        while True:
            try:
                self.betamount = int(input("Enter the bet amount: "))
                break
            except Exception as e:
                print("Enter a valid integer")
        rolls = self.startroll()
        print(f"The rolls are {rolls['dice1']}, {rolls['dice2']}, Totaling {rolls['total']}")
        while True:
            if rolls['total'] == 7 or rolls["total"] == 11:
                if bet == "pass line":
                    print(f"You win! You won {self.betamount * 2}")
                elif bet == "dont pass line":
                    print(f"You lose. You lost {self.betamount}")
                break
            elif rolls['total'] == 2 or rolls["total"] == 3:
                if bet == "pass line":
                    print(f"You lose. You lost {self.betamount}")
                elif bet == "dont pass line":
                    print(f"You win! You won {self.betamount * 2}")
                break
            elif rolls["total"] == 12:
                if bet == "pass line":
                    print(f"You lose! You lost {self.betamount}")
                elif bet == "dont pass line":
                    print(f"You tie. You win {self.betamount}") 
                break
            rolls = self.startroll()
        #Go to main play
    def play(self):
        while True:
            bet = input("Enter what bet you will do, The options are: Come bet, Dont come bet, Odds bet, Place bet, Field bets, Proposition bet, Hardaway bet or Hop bet: ").lower()
            if bet == "come bet":
                self.comebet()
            if bet == "dont come bet":
                self.dontcomebet()
            if bet == "odds bet":
                self.oddsbet()
            if bet == "place bet":
                self.placebet()
            if bet == "field bet":
                self.fieldbet()
            if bet == "proposition bet" or bet == "prop bet":
                self.propbet()
            if bet == "hardaway bet":
                self.hardbet()
            if bet == "hop bet":
                self.hopbet()
    def comebet(self):
        while True:
            try:
                self.betamount = int(input("Enter the bet amount: "))
                break
            except Exception as e:
                print("Enter a valid integer")
        rolls = self.startroll()
        print(f"The rolls are {rolls['dice1']}, {rolls['dice2']}, Totaling {rolls['total']}")
        while True:
            if rolls['total'] == 7 or rolls["total"] == 11:
                print(f"You win! You won {self.betamount * 2}")
                break
            elif rolls['total'] == 2 or rolls["total"] == 3:
                print(f"You lose. You lost {self.betamount}")
                break
            elif rolls["total"] == 12:
                print(f"You lose! You lost {self.betamount}")
                break
            rolls = self.startroll()
    def dontcomebet(self):
        while True:
            try:
                self.betamount = int(input("Enter the bet amount: "))
                break
            except Exception as e:
                print("Enter a valid integer")
        rolls = self.startroll()
        print(f"The rolls are {rolls['dice1']}, {rolls['dice2']}, Totaling {rolls['total']}")
        while True:
            if rolls['total'] == 7 or rolls["total"] == 11:
                print(f"You lose! You lose {self.betamount}")
                break
            elif rolls['total'] == 2 or rolls["total"] == 3:
                print(f"You win. You win {self.betamount*2}")
                break
            elif rolls["total"] == 12:
                print(f"You tie! You win {self.betamount}")
                break
            rolls = self.startroll()
    def oddsbet(self):
        #Once a point is made on the first roll or a come point on a succeeding roll, 
        # you may take the odds and win if the point or come points are made before a 7. 
        # Payoffs are: 2 to 1 on 4 and 10, 3 to 2 for 5 and 9, 6 to 5 on 6 and 8. 
        # “Don’t pass” or “don’t come” bets are in reverse: you must lay the odds in order to win.
        while True:
            try:
                self.betamount = int(input("Enter the bet amount: "))
                break
            except Exception as e:
                print(f"Enter a valid integer, {e}")
        while True:
            try:
                self.num = int(input("What number are you betting on? Payoffs are: 2 to 1 on 4 and 10, 3 to 2 for 5 and 9, 6 to 5 on 6 and 8: "))
                break
            except Exception as e:
                print(f"Enter a valid integer, {e}")
        while True:
            if rolls['total'] == 7:
                print(f"You lose {self.betamount}")
                break
            elif rolls['total'] == self.num:
                if self.num == 4 or self.num == 10:
                    print(f"You win {self.betamount * (2)}")
                if self.num == 5 or self.num == 9:
                    print(f"You win {self.betamount * 2 * (3/2)}")
                if self.num == 8 or self.num == 5:
                    print(f"You win {self.betamount *2 * (6/5)}")
                break
            rolls = self.startroll()
    def placebet(self):
        #Once a point is made on the first roll or a come point on a succeeding roll, 
        # you may take the odds and win if the point or come points are made before a 7. 
        # Payoffs are: 2 to 1 on 4 and 10, 3 to 2 for 5 and 9, 6 to 5 on 6 and 8. 
        # “Don’t pass” or “don’t come” bets are in reverse: you must lay the odds in order to win.
        while True:
            try:
                self.betamount = int(input("Enter the bet amount: "))
                break
            except Exception as e:
                print(f"Enter a valid integer, {e}")
        while True:
            try:
                self.num = int(input("What number are you betting on? Payoffs: 9 to 5 on 4 and 10, 7 to 5 on 5 and 9, and 7 to 6 on 6 and 8: "))
                break
            except Exception as e:
                print(f"Enter a valid integer, {e}")
        while True:
            if rolls['total'] == 7:
                print(f"You lose {self.betamount}")
                break
            elif rolls['total'] == self.num:
                if self.num == 4 or self.num == 10:
                    print(f"You win {self.betamount *(2) * (9/5)}")
                if self.num == 5 or self.num == 9:
                    print(f"You win {self.betamount * 2 * (7/5)}")
                if self.num == 8 or self.num == 5:
                    print(f"You win {self.betamount *2 * (7/6)}")
                break
            rolls = self.startroll()
    def fieldbet(self):
        #A one roll bet. You win even money on 3, 4, 9, 10 and 11. You win 2 to 1 on 2. You win 3 to 1 on 12. You lose on 5, 6, 7 or 8.        while True:
        while True:    
            try:
                self.betamount = int(input("Enter the bet amount. This is a one roll bet. You win even money on 3, 4, 9, 10 and 11. You win 2 to 1 on 2. You win 3 to 1 on 12. You lose on 5, 6, 7 or 8.: "))
                break
            except Exception as e:
                print(f"Enter a valid integer, {e}")
        rolls = self.startroll()
        if rolls["total"] == 3 or rolls["total"] == 4 or rolls["total"] == 9 or rolls["total"] == 10 or rolls["total"] == 11:
            print(f"You win back {self.betamount}")
        if rolls['total'] == 2:
            print(f"You win {self.betamount * 2}")
        if rolls['total'] == 12:
            print(f"You win {self.betamount * 3}")
        if rolls["total"] == 5 or rolls["total"] == 6 or rolls["total"] == 7 or rolls["total"] == 8:
            print(f"You lose {self.betamount}")
    def propbet(self):
        while True:    
            try:
                self.betamount = int(input("Enter the bet amount: "))
                break
            except Exception as e:
                print(f"Enter a valid integer, {e}")    
        call = input("What is your callout? Options: Any Craps (2,3,12), Aces (2), Twelve (12), Ace-Deuce (3), Eleven (11), or Seven (7):").lower()
        rolls = self.startroll()
        if rolls['total'] == 2 or rolls['total'] == 12 or rolls['total'] == 3:
            if call == "any craps":
                print(f"You win {self.betamount * 8}")
            elif rolls["total"] != 3:
                if call == "aces":
                    print(f"You win {self.betamount * 31}")
                if call == "twelve":
                    print(f"You win {self.betamount * 31}")
            elif rolls['total'] == 3:
                if call == "ace-deuce" or call == "ace deuce":
                    print("You win")
    def hardbet(self):
        #Hardaways
        #A Hardway bet is not a one-roll bet. 
        #You are betting that the shooter rolls a pair.
        #Hardways win if the dice roll as a pair and lose if a 7 rolls or if the number is thrown “the easy way.” 
        #Example: If you bet a hard 8 and thedice roll 4,4 you win. If the dice roll “easy” 5,3 or 6,2 you lose.
        #Hard Four or Ten 	pays 8 for 1
        #Hard Six or Eight 	pays 10 for 1   
        while True:
            betNum = str(input("Enter what number you will bet on: Hard 8, Hard 6, Hard 10 or Hard 4?: ")).lower()
            if betNum == "hard 8" or betNum == "hard 10" or betNum == "hard 6" or betNum == "hard 4":
                break
            else:
                print("Enter one of the options.")
        while True:
            try:
                self.betamount = int(input("Enter how much you will bet: "))
                break
            except:
                print("Enter a valid integer")
                
        x = int(betNum.split(" ")[1])
        easy = False
        rolls = self.startroll()
        while True:
            
            if rolls['dice1'] == rolls["dice2"]:
                break
                #elif rolls["total"] == 4 or rolls["total"] == 8 or rolls["total"] == 10 or rolls["total"] == 6: Doesnt work. In hindsight WHY WOULD THIS WORK???
                
            elif rolls["total"] == int(betNum.split(" ")[1]):
                easy = True
                break
            print(f"The roll is {rolls['dice1'],rolls['dice2']} totaling {rolls['total']}")
            rolls = self.startroll()
        if easy == True:
            print(f"You lose {self.betamount}, from {rolls['dice1'],rolls['dice2']} totaling {rolls['total']}")
        elif rolls["total"] == 4 or rolls["total"] == 10:
            if betNum == "hard 4" or betNum == "hard 10":
                print(f"You win {self.betamount * 8}, from {rolls['dice1'],rolls['dice2']} totaling {rolls['total']}")
        elif rolls["total"] == 6 or rolls["total"] == 8:
            if betNum == "hard 8" or betNum == "hard 6":
                print(f"You win {self.betamount * 10}, from {rolls['dice1'],rolls['dice2']} totaling {rolls['total']}")
    def hopbet(self):
        #Hop Bets are a one roll bet on a specific combination of the dice. 
        #You are literally betting on what you think the very next roll of the dice will be.
        #If you think the next roll is going to be a (6, 3), you would tell the dealer that you want the 6 and 3 hopping. 
        #Hop bets pay 31 for 1 or 16 for 1 depending on the combination that you choose.
        while True:
            try:
                betCombo = str(input("Enter what combination of two numbers you will bet on. Enter in the format: num1,num2 <- Seperate with comma; "))
                combo = betCombo.split(",")
                if len(combo) == 2 and int(combo[0]) > 0 and int(combo[0]) < 7  and int(combo[1]) > 0 and int(combo[1]) < 7:
                    break
            except:
                print("Enter in the valid format: num,num. Make sure that both numbers can be rolled by 1d6")
        while True:
            try:
                self.betamount = int(input("Enter how much you will bet: "))
                break
            except:
                print("Enter a valid integer")
        rolls = self.startroll()
        x = float(betCombo[1])
        combolistPlayer = [int(betCombo[0]), int(betCombo[1])]
        combolistComp = [int(rolls["dice1"]), int(rolls["dice2"])]
        print(combolistComp, combolistPlayer)


    
    def startroll(self):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
    
        return {"dice1":d1, "dice2": d2, "total": d1 + d2}


play = game()