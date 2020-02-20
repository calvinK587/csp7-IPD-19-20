####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Sasuke' # Only 10 chars displayed.
strategy_name = 'Sasuke Strategy'
strategy_description = 'How does this strategy decide?'

number_of_betrays = []

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    number_of_times_colluded = 0
    number_of_times_betrayed = 0
    for collude in their_history:
      if collude == "c":
        number_of_times_colluded += 1
    for betray in their_history:
      if betray == "b":
        number_of_times_betrayed += 1
    if number_of_times_betrayed > number_of_times_colluded:
      return 'c'
    else:
      return 'b'
    