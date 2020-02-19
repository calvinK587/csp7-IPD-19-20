####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'We_love_csp'
strategy_name = 'alternate until betrayed then betray'
strategy_description = 'our program will alternate. Though, if the other program betrays, then it will only betray'
def move(my_history, their_history, my_score, their_score):
   ''' Arguments accepted: my_history, their_history are strings.
   my_score, their_score are ints.
   Makes our move (Alternate until betrayed then betray).
   Returns 'c' or 'b' depending on what the opponent returns. 
   '''
   if 'b' in their_history: 
       return 'b'
       if len(my_history)%2 == 0:
           return 'c'
       else:
           return 'b'
   else: 
       return 'c'

