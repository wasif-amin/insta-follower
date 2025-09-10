from art import logo, vs
import random
from game_data import data

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description}, from {country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return  user_guess == "a"
    else:
        return user_guess == "b"



print(logo)
score = 0

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"compare A:{format_data(account_a)} ")
print(vs)
print(f"against B: {format_data(account_b)}")

guess = input("who has more followers? type A or B ").lower()

a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

is_correct = check_answer(guess, a_follower_count, b_follower_count)
if is_correct:
    score += 1
    print(f"correct score = {score}")

else:
    print(f"idiot, final score = {score}")

