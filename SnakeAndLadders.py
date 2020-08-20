class SnakesLadders():#since we have Ladders that take us up, and snakes that take us down - here are to dicts with las values. Also iy is possible to make just 1 dict.
    ladders = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}
    snakes = {16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80}

    def __init__(self):
        self.players = [0, 0]
        self.queue = [0, 1]
        self.turn = 0
        self.gamestate = 1

    def turnOrder(self, die1, die2):
        if die1 != die2:
            self.turn = (self.turn + 1) % 2# the TurnOrder function replaces players number

    def play(self, die1, die2):
        self.players[self.queue[self.turn]] += die1 + die2
        if self.players[self.queue[self.turn]] > 100:
            self.players[self.queue[self.turn]] = 200 - self.players[self.queue[self.turn]]
        if self.players[self.queue[self.turn]] in self.ladders:
            self.players[self.queue[self.turn]] = self.ladders[self.players[self.queue[self.turn]]]
        elif self.players[self.queue[self.turn]] in self.snakes:
            self.players[self.queue[self.turn]] = self.snakes[self.players[self.queue[self.turn]]]
        if self.players[self.queue[self.turn]] == 100 and self.gamestate == 1:
            self.gamestate = 3
            return "Player " + str(self.turn + 1) + " Wins!"
        elif self.gamestate == 3:
            return "Game over!"
        number = self.players[self.queue[self.turn]]
        turn = self.queue[self.turn]
        self.turnOrder(die1, die2)
        return "Player " + str(turn + 1) + " is on square " + str(number)

game = SnakesLadders()
print(game.play(X, Y)) # for X and Y we have die1 and die2 in this case