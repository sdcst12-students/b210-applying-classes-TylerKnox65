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
        #self.play()
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
        if rolls['total'] == 7 or rolls["total"] == 11:
           pass 
    def startroll(self):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
    
        return {"dice1":d1, "dice2": d2, "total": d1 + d2}


play = game()