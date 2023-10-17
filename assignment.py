#! python3
#Black Jack
import random
class game:
  def reset(self):
    self.ranks = ['Ace','2','3','4','5','6','7','8','9','Ten','Jack','Queen','King']
    #self.suits = ['C','D','H','S']
    self.clubs = [(i + " of Clubs") for i in self.ranks]
    self.diamonds = [(i + " of Diamonds") for i in self.ranks]
    self.hearts = [(i + " of Hearts") for i in self.ranks]
    self.spades = [(i + " of Spades") for i in self.ranks]
    self.all = [self.clubs, self.diamonds, self.hearts, self.spades]
    self.all = [i for i in (self.clubs + self.diamonds + self.hearts + self.spades)]
    self.bust = False
    self.compbust = False
    self.stand = False
    self.win = False
    self.hitV = True
    self.splitCards = False
    self.playerinput()
  def __init__(self,debug=False):
    if debug == False:
      self.reset()
    if debug == True:
      pass
      
  def playerinput(self):
    while True:
      playerin = input(f"{'_' * 147}\nWelcome to Blackjack! To view the rules type 'rules' to play type 'start': ")
      
      playerin = playerin.lower()
      if playerin == "start" or playerin == "":
        self.play()
      elif playerin == "rules" or playerin == "rule":
        print("\nThe aim of the game is to accumulate a higher point total than the dealer, but without going over 21. You compute your score by adding the values of your individual cards. The cards 2 through 10 have their face value, J, Q, and K are worth 10 points each, and the Ace is worth either 1 or 11 points (player's choice).")
        print("the player can keep his hand as it is (stand) or take more cards from the deck (hit), one at a time, until either the player judges that the hand is strong enough to go up against the dealer's hand and stands, or until it goes over 21, in which case the player immediately loses (busts).")
  def gethand(self,num=2):
      hand = []
      if num == 2:
        for i in range(2):
            hand1 = self.all[random.randint(0, len(self.all)-1)]
            self.all.pop(self.all.index(hand1))
            hand.append(hand1)
      elif num ==1:
        hand1 = self.all[random.randint(0, len(self.all)-1)]
        self.all.pop(self.all.index(hand1))
        hand.append(hand1)
      
      return(hand)
  def play(self):
    self.comphand = self.gethand()
    #self.comphand = ['3 of Hearts', '3 of Clubs']
    self.humanhand = self.gethand()
    #self.humanhand = ['6 of Spades', '7 of Spades']
    while True:
      try:
        self.bet = int(input("How much do you want to bet?: "))
        break
      except:
        print("Enter a valid integer.")
    print(self.humanhand)
    if list(self.humanhand[0])[0] == list(self.humanhand[1])[0]:
      playerin = input(f"Your hand is {self.humanhand}, the Dealer's shown card is the {self.comphand[1]}\nWhat do you want to do? (Stand, Hit or Split): ").lower()
      if playerin == "split":
       self.split()
        
    if True:
      while self.bust == False:
        self.playerturn()
      if self.win == True:
        print(f"You win! You won {self.bet * 2}, the computer's hand was {self.comphand}")
        self.reset()
      elif self.stand == True:
        while self.compbust == False:
          self.compturn()
        
        score = self.getvalue(self.humanhand, self.comphand)
        if score[1] < 21:
          if score[0] >= score[1]:
            print(f"You win! You won {self.bet * 2}, The computer's hand was the {self.comphand[0]} and the {self.comphand[1]}")
            self.reset()
          else:
            print(f"You lose! You lost {self.bet}, The computer's hand was {self.comphand} with value of {self.getvalue(self.humanhand, self.comphand)[1]}, Lose condition computer higher")
            self.reset()
        elif score[1] == 21:
          print(f"You lost {self.bet}, The computer's hand was the {self.comphand[0]} and the {self.comphand[1]}, meaning they got BlackJack")
          self.reset()
        else:
            print(f"You win! You won {self.bet * 2}, The computer's hand was {self.comphand}, With a value of {self.getvalue(self.humanhand, self.comphand)[1]} meaing they busted  ")

      else:
        print(f"You bust! You lost {self.bet}, Your hand was {self.humanhand} with value {self.getvalue(self.humanhand)}, The computer's hand was the {self.comphand[0]} and the {self.comphand[1]}")
        self.reset()
        
  def playerturn(self):
    values = self.getvalue(self.humanhand, self.comphand)#HUMAN FIRST COMP SECOND
    playerin = input(f"Your hand is {self.humanhand}, the value is {values[0]}. The Dealer's shown card is the {self.comphand[1]}\nWhat do you want to do? (Stand or Hit): ").lower()
    if playerin == "hit":
      self.hitTrue = True
      while self.hitTrue == True:
        if self.getvalue(self.humanhand) < 21:
          self.hit()
        if self.getvalue(self.humanhand) == 21:
          self.win = True
          self.bust = True
          break
        else:
          self.bust = True
          break
      self.bust = True
        
    elif playerin == "stand":
      self.stand = True
      self.bust = True
  
  
  def hit(self):
    temp = None
    if self.hitV == True and self.getvalue(self.humanhand) < 21:
      self.humanhand += self.gethand(1)
    if self.getvalue(self.humanhand) < 21:
      temp = input(f"Your hand is {self.humanhand}, the value is {self.getvalue(self.humanhand)}. The Dealer's shown card is the {self.comphand[1]}\nWhat do you want to do? (Stand or Hit): ").lower()
    elif self.getvalue(self.humanhand) >= 21:
      self.hitTrue = False
    if temp == "stand":
      self.hitTrue = False
    elif temp == "hit":
      self.hitV = True
      self.humanhand += self.gethand(1)
    
    
  def comphit(self):
    self.comphand += self.gethand(1)#Finish, calling for human. Dont know why I wrote this, Its calling for the computer?
    
  def compturn(self):
    #x = self.getvalue(self.humanhand,self.comphand)[1]
    if self.getvalue(self.humanhand,self.comphand)[1] < 16:
      self.comphit()
    else:
      self.compbust = True
  def getvalue(self, human, comp=None):
    valuesH = {'Ace ':11,'2 ':2,'3 ':3,'4 ':4,'5 ':5,'6 ':6,'7 ':7,'8 ':8,'9 ':9,'Ten ':10,'Jack ':10,'Queen ':10,'King ':10}
    valuesC = {'Ace ':11,'2 ':2,'3 ':3,'4 ':4,'5 ':5,'6 ':6,'7 ':7,'8 ':8,'9 ':9,'Ten ':10,'Jack ':10,'Queen ':10,'King ':10}
    humanvalue = []
    compvalue = []
    ace = False
    aceComp = False
    for i in human:
      
      humancard1 = i.split('of')
      if humancard1[0] == "Ace ":
        ace = True
      #print(humancard1)
      humanvalue.append(valuesH[humancard1[0]])
    if comp != None:
      for i in comp: #Gojo
        compcard1 = i.split('of')
        compvalue.append(valuesC[compcard1[0]])
        if compcard1[0] == "Ace ":
          aceComp = True
     
      humanvalue = sum(humanvalue)
      compvalue = sum(compvalue)
      if ace == True and humanvalue > 21:
        humanvalue -= 10
      if aceComp == True and compvalue > 21:
        compvalue -= 10
      return humanvalue, compvalue
    else:
      if ace == True and sum(humanvalue) > 21:
        return sum(humanvalue)-10
      else:
        return sum(humanvalue)
  def split(self): #I dont even want to think about this
    self.bet *= 2
    humanhand1 = [self.humanhand[0]]
    humanhand2 = [self.humanhand[1]]
    while self.splitCards == True:
      if self.getvalue(humanhand1) != 21 and self.getvalue(humanhand2) != 21:
        playerin = input(f"Your first hand is: {humanhand1} and the second hand is: {humanhand2}, the Dealer's shown card is the {self.comphand[1]}\nWhat do you want to do? (Stand, Hit or Split), to hit on a certain card enter 'hit left' or 'hit right': ").lower()
        if playerin == 'hit left':
          if self.getvalue(humanhand1) < 21:
            humanhand1 += self.gethand(1)
          elif self.getvalue(humanhand1) == 21:
            print("You have gotten blackjack on this hand already.")
          else:
            print("That hand has busted. You have lost the hand.")
        elif playerin == "hit right":
          if self.getvalue(humanhand2) < 21:
            humanhand2 += self.gethand(1)
          elif self.getvalue(humanhand2) == 21:
            print("You have gotten blackjack on this hand already.")
          
          else:
            print("That hand has busted. You have lost the hand.")
        
        elif playerin == "stand":
          self.bust = True
      elif self.getvalue(humanhand1) == 21 and self.getvalue(humanhand2) == 21:
        print(f"You got blackjack on both hands! You won {self.bet * 2}. Your hands were {humanhand1}, and {humanhand2}. The computer's hand was {self.comphand}")
        

# This is the only command allowed that is not in the class template. All code must be done there.

g = game(debug=False)
print(g.getvalue(['Queen of Hearts', '7 of Clubs'], ['3 of Hearts', '3 of Clubs']))
#g.play()
