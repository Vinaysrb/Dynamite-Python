import random

class DynamiteBot:
    def __init__(self):
        self.dynamite = 100

    def make_move(self, gamestate):
        if len(gamestate['rounds']) >= 1 and gamestate['rounds'][-1]['p1'] == gamestate['rounds'][-1]['p2'] and self.dynamite > 0:
            self.dynamite -= 1
            return 'D'

        list = [ "S", "P", "R"]   
        random_let = random.choice(list)
        return (random_let)
