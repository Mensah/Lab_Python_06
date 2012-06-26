"""
Lab_Python_06
Part 1
"""

import datetime

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure
player_name= ('rooney', 'ronaldo', 'torres')
scores = (2,2,0,3,0,1)
d1 = date(2012,06,23)
d2 = date(2012,06,25)
d3 = date(2012,06,19)
d4 = date(2012,06,20)
d5 = date(2012,06,21)

player_stats={player_name:{d1: score[0], d2:score[1]}, player_name:{d3: score[2], d4:score[3]}, player_name:{d5:[score[4],score[2]]}}

print player_stats

## implement highest_score
def highest_score(player_stats):
    
    

## implement highest_score_for_player
def highest_score_for_player(player_stats,player):


## implement highest_scorer
def highest_scorer(player_stats):
 #   scorer = player_stats
   # for i in player_stats:
#        if 
