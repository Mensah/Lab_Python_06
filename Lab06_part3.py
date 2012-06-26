class Team:
    def __init__(self,name,league,manager_name,points):
        self.name = name
        self.league = league
        self.manager_name = manager_name
        self.points = points
        self.players = []

    def add_player(self,player):
        playerr = self.players.append(player)
        return playerr

    def __str__(self):
        description = 
        
