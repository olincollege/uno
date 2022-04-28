import random
from uno_deck import Card, Deck

class GameState:
    
    def __init__(self):
        self.discard_pile = Deck(is_empty=True)
        self.draw_pile = Deck()
        self.draw_pile.shuffle()
        self.direction = 1
        self.current_action = None
        self.discard_pile.add_to_top(Card("Red","0"))
        self.won = False

    def reuse_discard_pile(self):
        top_card = self.discard_pile.draw()
        self.discard_pile.shuffle()
        useable_cards = self.discard_pile.cards
        for card in useable_cards:
            card.strip_chosen_color()
        self.draw_pile.add_to_bottom(useable_cards)
        self.discard_pile = Deck(def_cards=top_card)

    def current_color(self):
        return self.discard_pile.show_top().color

    def current_symbol(self):
        return self.discard_pile.show_top().symbol

    def __repr__(self):
        pass

class GameDirector:

    def __init__(self, player_list, game_state):
        self.game = game_state
        self.players = player_list
        self.current_player_index = 0
    
    def handle_reverse(self):
        if self.game.current_action == "Reverse":
            self.game.direction = -self.game.direction
            print("Reverse!")
            self.game.current_action = None
    
    def call_the_player(self):
        self.current_player().take_turn()
    
    def current_player(self):
        return self.players[self.current_player_index]

    def go_to_next_player(self):
        new_index = self.current_player_index + self.game.direction
        if new_index > 3:
            self.current_player_index = 0
        elif new_index < 0:
            self.current_player_index = 3
        else:
            self.current_player_index = new_index

    
