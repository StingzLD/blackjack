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
    # If the hand is a Blackjack
    if len(hand) == 2 and score == 21:
        score = 0
    # If the score is greater than 21 but there are aces
    elif score > 21 and 11 in hand:
        # Replace each ace until the hand is below is 21, if possible
        while 11 in hand:
            # Replace the first ace encountered with a 1
            for n in range(len(hand)):
                if hand[n] == 11:
                    hand[n] = 1
                    break
            # Recalculate hand score
            score = sum(hand)
            # If hand no longer busts, continue with the game
            if score <= 21:
                break
    return score


def show_blackjack():
    print(f"    Your hand: {player_hand}")
    print(f"    Dealer's hand: {dealer_hand}")


def show_hands():
    print(f"    Your hand: {player_hand}, Current score: {player_score}")
    print(f"    Dealer's first card: {dealer_hand[0]}")


def hit_or_pass():
    return (input("Type 'y' to get another card or 'n' to pass: ")).lower() == 'y'


def show_final_hands(msg=""):
    print(f"    Your final hand: {player_hand}, Final score: {player_score}")
    print(f"    Dealer's hand: {dealer_hand}, Final score: {dealer_score}")
    print(f"{msg}\n")


def play_again():
    print("Would you like to play again?")
    return (input("Type 'y' to play again or 'n' to end the game: ")).lower() == 'y'


# Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playing = True


# Main Code
while playing:
    clear_screen()
    print(logo)
    player_bust = False
    dealer_bust = False
    player_hand = []
    dealer_hand = []

    # Deal starting hands
    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    # Calculate starting hand scores
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    # Game logic if a hand has Blackjack
    if player_score == 0 or dealer_score == 0:
        show_blackjack()
        # Determine winner
        if player_score == 0 and dealer_score == 0:
            print("\n    Blackjack! It's a draw!\n")
        elif player_score == 0:
            print("\n    Blackjack! You win!\n")
        elif dealer_score == 0:
            print("\n    Blackjack! Dealer wins!\n")
        # Ask if the player wants to play again
        playing = play_again()
        continue

    # Show hands and ask if the player wants to hit
    # show_hands()
    show_final_hands()
    hit = hit_or_pass()

    # Continue dealing cards to the player until they no longer hit
    while hit:
        player_hand.append(deal_card())
        player_score = calculate_score(player_hand)
        # print(f"DEBUG: while hit")
        # print(f"DEBUG: Player's Hand: {player_hand}, Player's Score: {player_score}")
        if player_score < 21:
            show_hands()
            hit = hit_or_pass()
        elif player_score == 21:
            break
        else:
            player_bust = True
            break

    # Deal cards to dealer until they get higher than player or bust
    # Dealer must have a score higher than 16
    while dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)
        # print(f"DEBUG: while dealer_score < 17")
        # print(f"DEBUG: Dealer's Hand: {dealer_hand}, Dealer's Score: {dealer_score}")
        if dealer_score > 21:
            dealer_bust = True
            break

    # Dealer must have a higher score than player to win
    while not player_bust and dealer_score < player_score:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)
        # print(f"DEBUG: while dealer_score < player_score")
        # print(f"DEBUG: Dealer's Hand: {dealer_hand}, Dealer's Score: {dealer_score}")
        if dealer_score > 21:
            dealer_bust = True
            break

    # If both dealer and player bust, nobody wins
    if dealer_bust and player_bust:
        show_final_hands("Both Dealer and Player Bust! It's a draw!")
    # If only dealer bust, player wins
    elif dealer_bust:
        show_final_hands("Dealer busts! Player wins!")
    # If only player busted, dealer wins
    elif player_bust:
        show_final_hands("Player Busts! Dealer wins!")
    # If dealer has the higher score, dealer wins
    elif dealer_score > player_score:
        show_final_hands("Dealer wins!")
    # If player has the higher score, player wins
    elif player_score > dealer_score:
        show_final_hands("Player wins!")
    else:
        show_final_hands("It's a draw!")

    playing = play_again()
