# Strategy 1
import random
team_name = 'E0'
strategy_name = 'AnalyzingTendancies'
strategy_description = 'identifies the behavior of the opposing player, and then determines the strategy to compete against it, the way it does this is by analyszing tendancies shown in their past through counting the amount of colludes and betrays, and then making similar decisions'
    
def move(my_history, their_history, my_score, their_score):
  '''Make my move based on the history with this player.
  
  history: a string with one letter (c or b) per round that has been played with this opponent.
  their_history: a string of the same length as history, possibly empty. 
  The first round between these two players is my_history[0] and their_history[0]
  The most recent round is my_history[-1] and their_history[-1]
  
  Returns 'c' or 'b' for collude or betray.
  '''

  '''Initializes the counters for betray and collude'''
  collude_counter = 0
  betray_counter = 0

  #Loops throughout the history, to determine if they are typically an agressive colluder or betrayer, and by how much
  for decision in their_history:
    if decision == 'c':
      collude_counter+=1
    if decision == 'b':
      betray_counter += 1

  #First option is if the amount of times they collude is greater than the amount of times they betrayed
  if collude_counter>betray_counter:
    #Checking if they are an agressive colluder, meaning they collude more than 70%of the time
    if collude_counter/(collude_counter+betray_counter) > 0.7:
      final_decision = random.randint(1,10)
      if final_decision<8:
        #This if statment will become true 70% of the time to match the behavior of the other person
        return 'c'
      else:
        return 'b'
    else:
      final_decision = random.randint(1,10)
      if final_decision <7:
        return 'c'
      else:
        return 'b'

  #If they colluded and betrayed the same amount of times
  elif collude_counter == betray_counter:
    final_decision = random.randint(1,10)
    if final_decision <= 5:
      return 'c'
    else:
      return 'b'
  #If they were shown to betray more times than collude
  else:
    if betray_counter/(betray_counter+collude_counter) > 0.7:
      #Checking if they are an agressive betrayer, meaning they betrayer more than 70%of the time
      final_decision = random.randint(1,10)
      if final_decision <8:
        #This if statment will become true 70% of the time to match the behavior of the other person
        return 'b'
      else:
        return 'c'
    else:
      final_decision = random.randint(1,10)
      if final_decision <7:
        return 'c'
      else:
        return 'b'
