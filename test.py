def getvalue(humanhand, comphand):
    
    valuesH = {'Ace ':11,'2 ':2,'3 ':3,'4 ':4,'5 ':5,'6 ':6,'7 ':7,'8 ':8,'9 ':9,'Ten ':10,'Jack ':10,'Queen ':10,'King ':10}
    valuesC = {'Ace ':11,'2 ':2,'3 ':3,'4 ':4,'5 ':5,'6 ':6,'7 ':7,'8 ':8,'9 ':9,'Ten ':10,'Jack ':10,'Queen ':10,'King ':10}

    humancard1 = humanhand[0].split('of')
    humancard2 = humanhand[1].split('of')
    compcard1 = comphand[0].split('of')
    compcard2 = comphand[1].split('of')
    humanvalue = valuesH[humancard1[0]] + valuesH[humancard2[0]]
    compvalue = valuesC[compcard1[0]] + valuesC[compcard2[0]]
    print(humanvalue)#are you homeless
    if "Ace " in humancard1 and humanvalue > 21:
      valuesH['Ace'] = 1
      getvalue(['Ace of Hearts', 'Ace of Spades'],['6 of Hearts', '5 of Spades'])    
    if "Ace " in humanhand and humanvalue > 21:
      valuesH['Ace'] = 1
      getvalue(['Ace of Hearts', 'Ace of Spades'],['6 of Hearts', '5 of Spades']) 
getvalue(['Ace of Hearts', 'Ace of Spades'],['6 of Hearts', '5 of Spades'])

'''DOnt Need
    if "Ace" in human and humanvalue > 21:
      valuesH['Ace'] = 1
      self.getvalue(self.humanhand, self.comphand)    
    if "Ace" in human and humanvalue > 21:
      valuesH['Ace'] = 1
      self.getvalue(self.humanhand, self.comphand) 
'''
'''
            humancard1 = human[0].split('of')
            humancard2 = human[1].split('of')
            compcard1 = comp[0].split('of')
            compcard2 = comp[1].split('of')
            humanvalue = valuesH[humancard1[0]] + valuesH[humancard2[0]]
            compvalue = valuesC[compcard1[0]] + valuesC[compcard2[0]]
'''