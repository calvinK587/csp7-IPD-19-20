####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Sasuke' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
number_of_betrays = []

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    iterated_number = 0
    for b in their_history[-10]:
      if b == "b":
        iterated_number += 1
        number_of_betrays.append(iterated_number)
    if len(number_of_betrays) < 1:
      return 'c'
    else:
      for betray in number_of_betrays:
        return 'b'
      if 'b' not in their_history[-2:]:
        return 'c'
        number_of_betrays = []
