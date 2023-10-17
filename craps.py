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
    
    def startroll(self):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
    
        return {"dice1":d1, "dice2": d2, "total": d1 + d2}


play = game()