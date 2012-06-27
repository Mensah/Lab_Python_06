
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
        description ='The ' + self.name + ' team currently managed by  ' + self.manager_name + ', are at the top of their group table with ' + self.points + 'points in the ' + self.league + ' Cup'
        return description
        
        
Portugal = Team('Portugal', 'Euro2012','Boye Ferguson', '4')
Spain = Team('Espanyol', 'Euro2012','Nii Guardiola','6')
torres = Player('Fernando', 'Torres', Spain)
ronaldo = Player('Ronaldo', 'Cristiano', Portugal)
Spain.add_player(torres)

print Spain.players






    
