
class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team

    def add_score(self,score):
        self.scores.append(score)

    def total_score(self):
        t_score = (self.scores)
        return sum(t_score)

    def average_score(self):
        average = sum(self.scores)/float(len(self.scores))
        return average

    def __str__(self):
        
        description = 'Senior ' + self.first_name + ' ' + self.last_name + ', from ' + self.team
        return description

'''    
torres = Player('Fernando', 'Torres', Spain)
#print torres
spain = Player()

goals = int(raw_input('Please enter the number of scores you want to input: '))
print 'Please input them: '
for i in range(goals):
    s = int(raw_input())
    torres.add_score(s)


#torres.average_score()
print torres.scores
print torres.total_score()
print torres.average_score()
'''

class Team:
    def __init__(self,name,league,manager_name,points):
        self.name = name
        self.league = league
        self.manager_name = manager_name
        self.points = points
        self.players = []

    def add_player(self,player):
        self.players.append(player)

    def __str__(self):
        description = 'This is ' + self.players       
#        description ='The ' + self.name + ' team currently managed by  ' + self.manager_name + ', are at the top of their group table with ' + self.points + 'points in the ' + self.league + ' Cup'
        return description
        
        
Portugal = Team('Portugal', 'Euro2012','Boye Ferguson', '4')
Spain = Team('Espanyol', 'Euro2012','Nii Guardiola','6')
torres = Player('Fernando', 'Torres', Spain)
ronaldo = Player('Ronaldo', 'Cristiano', Portugal)
Spain.add_player(torres)
Portugal.add_player(ronaldo)


import datetime
class Match:
    def __init__(self, home_team, away_team, date):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.home_scores = {}
        self.away_scores = {}

    def home_score(self):
        t_home_score = []
        for i in self.home_scores:
            if len(self.home_scores) > 0:
                r = self.home_score[i]
                t_home_score.append(r)

            else:
                r = self.home_score[i]
                r = 0
                t_home_score.append(r)
                
        return sum(t_home_score)
        

    def away_score(self):
        t_away_score = []
        for i in self.away_score:
            if len(self.away_scores) > 0:
                r = self.away_score[i]
                t_away_score.append(r)

            else:
                r = self.away_score[i]
                r = 0
                t_away_score.append(r)
                
        return sum(t_away_score)

    def winner(self):
        h = sum(self.home_scores.values())
        a = sum(self.away_scores.values())
        if a<h:
            return self.home_team
        elif a>h:
            return self.away_team
        else:
            return 'Draw'

    def add_score(self,player,score):
        self.player = player
        self.score = score
        score = 1
        if player.team == self.home_team: 
            self.home_scores[player] = [score]
        elif player.team == self.away_team:
            self.away_scores[player] = [score]

    def __str__(self):
        des = 'And the winner is ' + 

euro_semi_final = Match(Spain, Portugal, datetime.date('2012', 'June', '27'))



euro_semi_final.add_score(torres, 1)
euro_semi_final.add_score(ronaldo,1)
euro_semi_final.add_score(torres, 1)

print winner()






    
