####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####


team_name = 'God Tier Masters' # Only 10 chars displayed.
strategy_name = 'Kindest Betrayer'
strategy_description = 'This player does the opposite of the previous action by the opponent and looks for betrayals from opponent and copies the betrayal on the next turn.'

    
def move(my_history, their_history, my_score, their_score):
  ''' Arguments accepted: my_history, their_history are strings.
  my_score, their_score are ints.
  
  Make my move.
  Returns 'c' or 'b'. 
  '''

  # my_history: a string with one letter (c or b) per round that has been played with this opponent.
  # their_history: a string of the same length as history, possibly empty. 
  # The first round between these two players is my_history[0] and their_history[0].
  # The most recent round is my_history[-1] and their_history[-1].

  # This player does the opposite of the previous action by the opponent
  #Added change included and
  #Added change looks for betrayals from opponent and copies the betrayal on the next turn
  if len(my_history)==0:
    return 'c'
  elif their_history[-1]=='c' and 'b' in their_history[-3:]:
    return 'b'
  else:
    return 'c'

