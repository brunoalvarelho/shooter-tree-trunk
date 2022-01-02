from src.model.player import Player


class Game:
    def __init__(self):
        self.keyPressed = {}
        # generate player
        self.player = Player()
