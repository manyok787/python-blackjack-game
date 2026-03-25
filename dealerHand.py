
from TheHandClass import Hand


class DealerHand(Hand):
    def __init__(self):
        super().__init__()
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
    
    def show_first_card(self):
        if self.cards:
            return str(self.cards[0])
        return "No cards in hand."
    
    def __str__(self):  # show representation of dealer's hand
        res = ['Dealer Hand:']
        for card in self.cards:
            res.append(str(card))
        res.append(f'Total Value: {self.calculate_value()}')
        return '\n'.join(res)