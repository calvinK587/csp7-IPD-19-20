####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'S & Y' # Only 10 chars displayed.

strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):

  ''' This strategy works based on the other person's score. If my score is less then theirs, then it will betray. If my score is greater than theirs, then it will collude. '''
  if my_score <= their_score:
    return "b"
  elif my_score >= their_score:
    return 'c'
  else:
    return 'b'
  if my_score <= -5000 and their_score >= my_score:
    return 'b'


