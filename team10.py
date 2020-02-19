####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Friendlies' # Only 10 chars displayed.
strategy_name = 'Do Not Stop'
strategy_description = 'The strategy will collude on the first round, but then betrays on every round after that.'
    
def move(my_history, their_history, my_score, their_score):
  '''On the first round, it should collude, but after the first round, it should only betray.'''
  if len(my_history) == 0:
    return 'c'
  else:
    return 'b'
