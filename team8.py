####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Baboons'
strategy_name = 'Collude and then betray'
strategy_description = '''collude the first round. If they betray more than 20 times, then we betray. \n'''
    
def move(my_history, their_history, my_score, their_score):
  '''initiates strategy <Collude and then betray> '''
  theirB = 0
  if len(my_history) == 0:
      return 'c'
  for action in their_history:
    if action == 'b':
      theirB+=1 
  if theirB >= 20: 
      return 'b'        
  else:
      return 'c'

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    

