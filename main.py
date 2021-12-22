#Display Art
from art import logo,vs
print(logo)
from game_data import data
import random

def format_data(account):
    """Takes the account data and returns into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(guess, a_followers, b_followers): 
    """Take user guess and follower account and returns if they got it right"""
    if a_followers > b_followers: 
        return guess == "a"
    else: 
        return guess == "b"

score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    #Generate random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #Ask the user for the guess
    guess = input("Who has more followers? Type 'A' or 'B' ").lower()

    #Check whether the user guess is correct or wrong
    ##Get the follower account of each account
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    ##Use if statements to check whether the user guess is correct

    is_correct = check_answer(guess, a_follower_account, b_follower_account)
    
    #Give user the feedback
    if is_correct:
        score+=1
        print(f"You're right! Current score: {score}")
    else: 
        game_should_continue = False
        print(f"You're wrong!Final score: {score}")


