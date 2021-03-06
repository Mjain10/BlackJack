import random
import sys

print()
print("Welcome to Python Blackjack!")
print()


cards = ['2', '2', '2', '2',
         '3', '3', '3', '3',
         '4', '4', '4', '4',
         '5', '5', '5', '5',
         '6', '6', '6', '6',
         '7', '7', '7', '7',
         '8', '8', '8', '8',
         '9', '9', '9', '9',
         '10', '10', '10', '10',
         '10', '10', '10', '10',
         '10', '10', '10', '10',
         '10', '10', '10', '10',
         'Ace', 'Ace', 'Ace', 'Ace']


def dealer_hand() -> list:
    print()
    print("Dealer's hand:")
    print('-------------')
    return deal_cards()

        

def player_hand() -> list:
    print()
    print("Player's hand:")
    print('-------------')
    return deal_cards()
   
    

          
def deal_cards() -> list:
    temp = []
    hand = []
    print()
    print("*Dealt hand*")
    for i in range(2):
        cards_dealt = random.choice(cards)
        print(
            cards_dealt)
        temp.append(cards_dealt)
        cards.remove(cards_dealt)
    print()
    print("*Current hand:(after any aces have been converted)*")
    for card in temp:
        if card == 'Ace':
           value = int(input("Ace = 1 or 11? "))
           if value == 1:
               hand.append(1)
           if value == 11:
               hand.append(11)         
        else:
            hand.append(int(card))
            
    for card in hand:
        print( card)
        
    return hand




def total(L) -> int:
    total = 0
    for card in L:
        total += card

    print()
    print("Total hand value:")
    print( total)

    if total == 21:
       print("Blackjack!")
       another_round()
    else:
        pass
    
    return total




def hit_player():
    global final
    final = 0
    print("Player's Turn")
    print('-------------')
    current_hand = player_hand() #list
    hand_total = total(current_hand) #int
    print()
    while True:            
        ask = input("Hit or stand? ")
        if ask == "hit":
            new_card = random.choice(cards)
            if new_card == "Ace":
                value = int(input("Ace = 1 or 11? "))
                if value == 1:
                    current_hand.append(1)
                    hand_total += 1
                if value == 11:
                    current_hand.append(11)
                    hand_total += 11
            else:
                current_hand.append(new_card)
                hand_total += int(new_card)
                
            for card in current_hand:
                print( card)
            print("Total hand value:")
            print( hand_total)


            if hand_total == 21: 
                print("Blackjack! Player wins!")
                another_round()
            else:
                pass
                           
            
            if hand_total > 21:
                print()
                print("Busted!")
                print("Dealer wins!")
                another_round()
            else:
                continue

    
        elif ask == "stand":
            final += hand_total
            hit_dealer()
  

def hit_dealer():
    print("Dealer's Turn")
    print('-------------')
    current_hand2 = dealer_hand() #list
    hand_total2 = total(current_hand2) #int
    print()
    while True:
        ask2 = input("Hit or stand? ")
        if ask2 == "hit":
            if hand_total2 < 17:
                new_card2 = random.choice(cards)
                if new_card2 == "Ace":
                    value2 = int(input("Ace = 1 or 11? "))
                    if value2 == 1:
                        current_hand2.append(1)
                        hand_total2 += 1
                    if value2 == 11:
                        current_hand2.append(11)
                        hand_total2 += 11
                else:
                    current_hand2.append(new_card2)
                    hand_total2 += int(new_card2)
            else:
                print("Dealer has already reached 17 or more points")
                pass

            for card in current_hand2:
                    print(card)
            print("Total hand value:")
            print( hand_total2)


            if hand_total2 == 21: 
                print("Blackjack! Dealer wins!")
                another_round()
            else:
                pass
                               

            if hand_total2 > 21:
                print()
                print("Busted!")
                print("Dealer loses! Player wins!")
                another_round()
            else:
                continue
            
    
        elif ask2 == "stand":
            if final == hand_total2:
                print("Push")
                another_round()
            if final < hand_total2:
                print("Dealer wins!")
                another_round()
            if final > hand_total2:
                print("Player wins!")
                another_round()
            

def another_round():
    again = input("Would you like to play again? Yes or no? ")
    if again == "yes":
        hit_player()
    elif again == "no":
        sys.exit()


           
if __name__ == '__main__':
    hit_player()
    

    
    






