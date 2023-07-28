class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self):
        self.choice = input(
            "{name}, select rock, paper, scissor, lizard or spock: ".format(
                name=self.name
            )
        )
        print("{name} selects {choice}".format(name=self.name, choice=self.choice))

    def toNumbericalChoice(self):
        switcher = {"rock": 0, "paper": 1, "scissor": 2, "lizard": 3, "spock": 4}
        return switcher[self.choice]

    def incrementPoint(self):
        self.points += 1
