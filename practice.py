class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"


emp_1 = Employee('Candace', 'Andrews', 50000)
emp_2 = Employee('Corey', 'Schafer', 60000)

print(emp_1.email)
print(emp_2.email)




hand_value = 0
aces = 0

for card in self.hand:
    if card.rank == 'A':
        aces +=1
    elif card.rank in ['K', 'Q', 'J']:
        hand_value +=10
    else:
        hand_value += card.rank
for _ in range(aces):
    if hand_value + 11 > 21
        hand_value += 1
    else:
        hand_value += 11
    return hand_value





self.deck.shuffle()

while len(player.hand) > 2 and len(dealer.hand) < 2:
    





if self.dealer.calculate() <21:
    if self.dealer.hand.append(card)
    print('dealer hand is: ')
    self.dealer.view_cards()
elif self.dealer.calculate() > 21:
    print("dealer bust")
    return self.dealer.calculate()


player_turn(self, stay)


def turn_take(self):
    p_score = 0
    d_score = 0
    stay = False
    while p_score < 21 and stay == False:
    p_score = self.player_turn()
    while d_score < 17:
        d_score = self.dealer_turn()