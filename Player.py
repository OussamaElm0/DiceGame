class Player :
    listPlayers = []

    def __init__(self, playerName):
        self.name = playerName
        self.score = 0
        self.tour = 0

    def play(self,dice):
        self.tour += 1
        if self.tour > 3 :
            return "You have already play tours."
        self.score += dice[0] + dice[1]
        return  f"Your current score is {self.score}"

    @staticmethod
    def addPlayer(obj):
        Player.listPlayers.append(obj)

    @staticmethod
    def showWinner():
        score1 = Player.listPlayers[0].score
        score2 = Player.listPlayers[1].score
        if score1 < score2 :
            print(f'Winner is {Player.listPlayers[1].name}')
        else :
            print(f'Winner is {Player.listPlayers[0].name}')

    def __str__(self):
        return  f'Name: {self.name} \nScore: {self.score} \nTour: {self.tour}'