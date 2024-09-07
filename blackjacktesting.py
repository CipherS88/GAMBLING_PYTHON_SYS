import tkinter as tk
import random

# Card values and symbols
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

SUIT_SYMBOLS = {
    'Hearts': '♥',
    'Diamonds': '♦',
    'Clubs': '♣',
    'Spades': '♠'
}

# Deck creation
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    return [f'{value} of {suit}' for suit in suits for value in CARD_VALUES.keys()]

class BlackjackGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Blackjack Game by Nowibe Coder")
        
        self.balance = 1000
        self.bet = 0
        self.deck = create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = True
        
        self.setup_ui()

    def setup_ui(self):
        self.balance_label = tk.Label(self.master, text=f'Balance: ${self.balance}', font=('Arial', 14))
        self.balance_label.pack(pady=10)
        
        self.bet_entry = tk.Entry(self.master, font=('Arial', 14))
        self.bet_entry.pack(pady=10)
        self.bet_entry.insert(0, "Enter your bet (1-1000)")
        
        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game, font=('Arial', 14))
        self.start_button.pack(pady=10)

        self.player_label = tk.Label(self.master, text="", font=('Arial', 14))
        self.player_label.pack(pady=10)

        self.dealer_label = tk.Label(self.master, text="", font=('Arial', 14))
        self.dealer_label.pack(pady=10)

        self.hit_button = tk.Button(self.master, text="Hit", command=self.hit, state=tk.DISABLED, font=('Arial', 14))
        self.hit_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.stand_button = tk.Button(self.master, text="Stand", command=self.stand, state=tk.DISABLED, font=('Arial', 14))
        self.stand_button.pack(side=tk.RIGHT, padx=20, pady=20)

        self.result_label = tk.Label(self.master, text="", font=('Arial', 14))
        self.result_label.pack(pady=10)

    def start_game(self):
        try:
            self.bet = int(self.bet_entry.get())
            if 1 <= self.bet <= self.balance:
                self.balance -= self.bet
                self.balance_label.config(text=f'Balance: ${self.balance}')
                self.deck = create_deck()
                random.shuffle(self.deck)
                self.player_hand = [self.deck.pop(), self.deck.pop()]
                self.dealer_hand = [self.deck.pop(), self.deck.pop()]
                self.game_over = False

                self.update_hands()
                self.hit_button.config(state=tk.NORMAL)
                self.stand_button.config(state=tk.NORMAL)
                self.result_label.config(text="")
            else:
                self.result_label.config(text="Invalid bet! Enter a number between 1 and 1000.")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def update_hands(self):
        player_hand_symbols = self.cards_to_symbols(self.player_hand)
        dealer_hand_symbols = self.cards_to_symbols(self.dealer_hand[:1]) + " ??"
        self.player_label.config(text=f'Your Hand: {player_hand_symbols} (Score: {self.calculate_score(self.player_hand)})')
        self.dealer_label.config(text=f'Dealer Hand: {dealer_hand_symbols}')

    def cards_to_symbols(self, hand):
        return ' '.join(f"{value}{SUIT_SYMBOLS[suit]}" for card in hand for value, suit in [card.split(' of ')])

    def calculate_score(self, hand):
        score = sum(CARD_VALUES[card.split()[0]] for card in hand)
        aces = hand.count('A of Hearts') + hand.count('A of Diamonds') + hand.count('A of Clubs') + hand.count('A of Spades')
        while score > 21 and aces:
            score -= 10
            aces -= 1
        return score

    def hit(self):
        if not self.game_over:
            self.player_hand.append(self.deck.pop())
            player_score = self.calculate_score(self.player_hand)

            if player_score > 21:
                self.result_label.config(text="You busted! Dealer wins!")
                self.game_over = True
                self.hit_button.config(state=tk.DISABLED)
                self.stand_button.config(state=tk.DISABLED)
            else:
                self.update_hands()

    def stand(self):
        if not self.game_over:
            dealer_score = self.calculate_score(self.dealer_hand)
            while dealer_score < 17:
                self.dealer_hand.append(self.deck.pop())
                dealer_score = self.calculate_score(self.dealer_hand)

            self.update_final_hands(dealer_score)

    def update_final_hands(self, dealer_score):
        dealer_hand_symbols = self.cards_to_symbols(self.dealer_hand)
        self.dealer_label.config(text=f'Dealer Hand: {dealer_hand_symbols} (Score: {dealer_score})')
        player_score = self.calculate_score(self.player_hand)

        if dealer_score > 21 or player_score > dealer_score:
            self.result_label.config(text="You win!")
            self.balance += self.bet * 2
        elif player_score < dealer_score:
            self.result_label.config(text="Dealer wins!")
        else:
            self.result_label.config(text="It's a tie!")
            self.balance += self.bet

        self.balance_label.config(text=f'Balance: ${self.balance}')
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.game_over = True

if __name__ == "__main__":
    root = tk.Tk()
    game = BlackjackGame(root)
    root.mainloop()
