import art
import gamedata
import random
import clear

print(art.logo)
score = 0
cont = False

while not cont:

    comp1 = random.choice(gamedata.data)
    comp2 = random.choice(gamedata.data)

    print(f"Compare A: {comp1["name"]}, a {comp1["description"]}, from {comp1["country"]}.")
    print(art.vs)
    print(f"Compare B: {comp2["name"]}, a {comp2["description"]}, from {comp2["country"]}.")

    user_input = input("Who has more followers? Type 'A' or 'B':").lower()
    if "a" in user_input and comp1["follower_count"] > comp2["follower_count"]:
        score += 1
        clear.clear()
        print(f"You're right! Current score: {score}.")
    elif "b" in user_input and comp1["follower_count"] < comp2["follower_count"]:
        score += 1
        clear.clear()
        print(f"You're right! Current score: {score}.")
    elif "a" in user_input and comp1["follower_count"] < comp2["follower_count"]:
        print(f"Sorry, that's wrong. Final score: {score}")
        cont = True
        clear.clear()
    elif "b" in user_input and comp1["follower_count"] > comp2["follower_count"]:
        print(f"Sorry, that's wrong. Final score: {score}")
        cont = True
        clear.clear()
