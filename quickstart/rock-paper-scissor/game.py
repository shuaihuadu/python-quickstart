from participant import Participant
from gameRound import GameRound


class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Krik")

    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue game y/n: ")
        if answer == "y":
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print(
                "Game ended,{p1name} has {p1points}, and {p2name} has {p2points}".format(
                    p1name=self.participant.name,
                    p1points=self.participant.points,
                    p2name=self.secondParticipant.name,
                    p2points=self.secondParticipant.points,
                )
            )
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.secondParticipant.name)
        print(resultString)
