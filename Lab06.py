import datetime
class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team

    def add_score(self,score):
        scoree = self.scores.append(score)
        return scoree

    def total_score(self):
        t_score = sum(self.scores)
        return t_score

    def average_score(self):
        average = total_score/len(self.scores)
        return average

    def __str__(self):
        
       # description = 'Senior ' + self.first_name + ' ' + self.last_name + ', the ' + self.team
        return description

    
torres = Player('Fernando', 'Torres', 'Espanyol')
#print torres

goals = int(raw_input('Please enter the number of scorec you want to input: '))
print 'Please input them: '
for i in range(goals):
    s = int(raw_input())
    torres.add_score(s)


#torres.average_score()
print torres.scores
print torres.total_score



    
