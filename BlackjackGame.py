
'''
class to simulate a simple blackjack game
initialized with a deck of cards and two players (dealer and user)
deals two cards to each player and allows user to hit or stand
determines the winner based on blackjack rules
'''
import TheDeckClass
import dealerHand
import playerHand

class BlackJackGame:
    def __init__(self):
        #create and shuffle deck
        self.deck = TheDeckClass.Deck(TheDeckClass.Deck.make_cards())
        self.deck.shuffle()
        #create dealer and player hands
        self.dealer_hand = dealerHand.DealerHand()
        self.player_hand = playerHand.PlayerHand(player_id=1)

    def deal_initial_hands(self):
        #deal two cards to each player
        self.deck.move_cards(self.player_hand, 2)
        self.deck.move_cards(self.dealer_hand, 2)
            
    def player_turn(self):
        while True:
            print(self.player_hand)
            choice = input("Do you want to hit or stand? (h/s): ").lower()
            if choice == 'h':
                self.deck.move_cards(self.player_hand, 1)
                if self.player_hand.calculate_value() > 21:
                    print(self.player_hand)
                    print("Player busts! Dealer wins.")
                    return False
            elif choice == 's':
                break
            else:
                print("Invalid choice. Please enter 'h' or 's'.")
        return True
    
    def dealer_turn(self):
        while self.dealer_hand.calculate_value() < 17:
            self.deck.move_cards(self.dealer_hand, 1)
        print(self.dealer_hand)
        if self.dealer_hand.calculate_value() > 21:
            print("Dealer busts! Player wins.")
            return False
        return True

    def determine_winner(self):

        player_value = self.player_hand.calculate_value()

        dealer_value = self.dealer_hand.calculate_value()

        if player_value > dealer_value:
            print("Player wins!")
        elif dealer_value > player_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")
            
        
    def play(self):
        self.deal_initial_hands()
        print("Dealer's first card:")
        print(self.dealer_hand.show_first_card())
        if not self.player_turn(): # player busts
            return
        if not self.dealer_turn(): # dealer busts
            return
        self.determine_winner()

if __name__ == "__main__":
    game = BlackJackGame()
    game.play()