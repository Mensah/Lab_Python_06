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
        
        

Spain = Team('Espanyol', 'Euro2012','Nii Guardiola','6')
print Spain
