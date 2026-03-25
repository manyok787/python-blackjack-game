

from TheHandClass import Hand


class PlayerHand(Hand):
    def __init__(self, player_id):
        super().__init__()
        self.player_id = player_id
        self.cards = []

    def calculate_value(self):
        value = 0
        for card in self.cards:
            # ace can either be 1 or 11
            if card.rank == 14:
                value += 11 if value + 11 <= 21 else 1
            elif card.rank >= 10:
                value += 10
            else:
                value += card.rank
        return value
    
    def __str__(self): # show representation of player's hand
        res = [f'Player {self.player_id} Hand:']
        for card in self.cards:
            res.append(str(card))
        res.append(f'Total Value: {self.calculate_value()}')
        return '\n'.join(res)