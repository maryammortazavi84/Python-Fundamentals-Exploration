from random import choice

class French_deck:
    ranks = [str(n) for n in range(2,11)] + list("JKQA")
    suits = ["clubs" , "spades", "dimonds", "hearts"]

    def __init__(self):
        self._cards = [(rank, suit) for suit in self.suits
                                    for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self , position):
        return self._cards[position]



deck = French_deck()
print(len(deck))
print(deck[5])
print(choice(deck))

