class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0],
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print(
            "Round resulted in a {result}".format(result=self.getResultAsString(result))
        )
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()
        else:
            print("No points for anybody.")

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumbericalChoice()][p2.toNumbericalChoice()]

    def awardPoints(self):
        print("implement")

    def getResultAsString(self, result):
        res = {0: "draw", 1: "win", -1: "loss"}
        return res[result]
