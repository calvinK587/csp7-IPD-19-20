####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Sasuke' # Only 10 chars displayed.
strategy_name = 'if this wins, follow @an9sh on instagram'
strategy_description = 'Counts the number of times the other person has betrayed and continues to betray that many times. Starts with collude.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move. In order to make a move, this strategy looks at past data, and makes a variable which counts the number of times they have betrayed in the past. Then, the algorithmn betrays the same number of time the other competitior has betrayed. The number of betrays queued will reset if the opponent colludes twice in a row.

    Math:
    betray = n
    betray to the nth multiple
    
    Returns 'c' or 'b'. 
    '''
    number_of_betrays = 0
    iterated_number = 0
    for b in their_history:
      if b == "b":
        iterated_number += 1
        number_of_betrays += 1
    if number_of_betrays < 1:
      return 'c'
    else:
      while number_of_betrays > 0:
        return 'b'
        number_of_betrays -= 1
         
      if 'b' not in their_history[-2:]:
        return 'c'
        number_of_betrays = 0

