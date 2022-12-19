import os
import random
from art import logo


# Functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card():
    return random.choice(cards)


def calculate_score(hand):
    score = sum(hand)
    if len(hand) == 2 and score == 21:
        score = 0
    elif score > 21 and 11 in hand:
        score -= 10
    return score


def show_blackjack():
    print(f"    Your hand: {player_hand}")
    print(f"    Dealer's hand: {dealer_hand}")


# Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playing = True


# Main Code
while playing:
    print(logo)
    player_hand = []
    dealer_hand = []

    # Deal starting hands
    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    # Calculate starting hand scores
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    # Check for hand(s) with Blackjack
    if player_score == 0 and dealer_score == 0:
        show_blackjack()
        print("\n    Blackjack! It's a draw!")
        break
    elif player_score == 0:
        show_blackjack()
        print("\n    Blackjack! You win!")
        break
    elif dealer_score == 0:
        show_blackjack()
        print("\n    Blackjack! Dealer wins!")
        break

    # Print player's hand, player's score, and dealer's first card
    print(f"    Your hand: {player_hand}, Current score: {player_score}")
    print(f"    Dealer's first card: {dealer_hand[0]}")

    # Ask player if they want to hit
    hit = input("Type 'y' to get another card or 'n' to pass: ") == 'y'
    if hit:
        player_hand.append(deal_card())
        player_score = calculate_score(player_hand)
        print(f"    Your hand: {player_hand}, Current score: {player_score}")
        print(f"    Dealer's first card: {dealer_hand[0]}")
    else:
        print(f"    Your final hand: {player_hand}, Final score: {player_score}")
        # TODO Deal cards to dealer until they get higher than player or busts
        print(f"    Dealer's hand: {dealer_hand}, Final score: {dealer_score}")

