#100DaysOfCode
#TheAppBrewery

from art import logo
import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear():
    os.system('cls')


def final_count():
    if player_score > 21:
        print("You lose")
    elif computer_score > 21:
        print("You win!")
    elif player_score > computer_score:
        print("You win!")
    elif player_score < computer_score:
        print("You lose")
    else:
        print("It's a draw")


print(logo)

continue_game = True
while continue_game:
    player_hand = []
    computer_hand = []
    player_score = 0
    computer_score = 0
    start = input("Do you want to play a game of Blackjack? Type 'yes' or 'no'.\n")
    if start == 'yes':
        clear()
        player_hand.append(random.choice(cards))
        player_hand.append(random.choice(cards))
        for card in player_hand:
            player_score += card
        print(f"Your cards are {player_hand}. Your current score is {player_score}.")
        computer_hand.append(random.choice(cards))
        computer_hand.append(random.choice(cards))
        for card in computer_hand:
            computer_score += card
        print(f"Computer's first card is {computer_hand[0]}.")
        more_cards = True
        while more_cards:
            if player_score == 21:
                more_cards = False
                print(f"Your final hand is {player_hand} and your final score is {player_score}.")
                while computer_score < 17:
                    computer_hand.append(random.choice(cards))
                    computer_score += computer_hand[len(computer_hand) - 1]
                    for value in computer_hand:
                        if computer_score > 21 and value == 11:
                            index = computer_hand.index(11)
                            computer_hand.remove(11)
                            computer_score -= 11
                            computer_hand.insert(index, 1)
                            computer_score += 1
                print(f"Computer's final hand is {computer_hand} and it's final score is {computer_score}.")
                final_count()
                break
            another_card = input("Type 'yes' to get another card, type 'no' to pass.\n")
            if another_card == "yes":
                player_hand.append(random.choice(cards))
                player_score += player_hand[len(player_hand) - 1]
                for value in player_hand:
                    if player_score > 21 and value == 11:
                        index = player_hand.index(11)
                        player_hand.remove(11)
                        player_score -= 11
                        player_hand.insert(index, 1)
                        player_score += 1
                print(f"Your cards are {player_hand}. Your current score is {player_score}.")
                print(f"Computer's first card is {computer_hand[0]}.")
                if player_score > 21:
                    more_cards = False
                    print(f"Your final hand is {player_hand} and your final score is {player_score}.")
                    print(f"Computer's final hand is {computer_hand} and it's final score is {computer_score}.")
                    print("You lose")
                    break
            elif another_card == "no":
                more_cards = False
                print(f"Your final hand is {player_hand} and your final score is {player_score}.")
                for value in computer_hand:
                    if computer_score > 21 and value == 11:
                        index = computer_hand.index(11)
                        computer_hand.remove(11)
                        computer_score -= 11
                        computer_hand.insert(index, 1)
                        computer_score += 1
                while computer_score < 17:
                    computer_hand.append(random.choice(cards))
                    computer_score += computer_hand[len(computer_hand) - 1]
                    for value in computer_hand:
                        if computer_score > 21 and value == 11:
                            index = computer_hand.index(11)
                            computer_hand.remove(11)
                            computer_score -= 11
                            computer_hand.insert(index, 1)
                            computer_score += 1
                print(f"Computer's final hand is {computer_hand} and it's final score is {computer_score}.")
                final_count()
            else:
                more_cards = False
                print("Invalid option, you lose.")
    elif start == 'no':
        continue_game = False
        print("The game was shutdown.")
    else:
        continue_game = False
        print("Invalid option. The game was shutdown.")
