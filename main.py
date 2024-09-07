import math
import random

tabelofgames = ["777", "blackjcak21", "R P S"]
wallet = 100

print(f"Welcome to this simple game. We have {tabelofgames[0]}, {tabelofgames[1]}, and {tabelofgames[2]}")
playerchosie = int(input(f"ENTER 1 TO PLAY {tabelofgames[0]}."
                         f" ENTER 2 TO PLAY {tabelofgames[1]}."
                         f" ENTER 3 TO PLAY {tabelofgames[2]}:"))


def coregame():
    global wallet

    if playerchosie == 1:
        print("You have chosen 777. The idea is simple: "
              "\n3 random numbers will be generated. 777 means wallet x100."
              " Two same numbers = +50%, and different numbers mean loss of 50%.")

        play777 = input("Enter 'y' if you are ready: ").lower()

        if play777 == "y":
            print("number being generated.>>>>>>>")
            x777 = random.randint(1, 9)
            y777 = random.randint(1, 9)
            z777 = random.randint(1, 9)
            wincheck777 = f"{x777}{y777}{z777}"

            print(f"the 1st n: {x777} \nthe 2nd n: {y777} \nthe 3rd n: {z777}")

            if wincheck777 == "777":
                wallet *= 100
                print(f"You win x100! New wallet balance: {wallet}")
            elif wincheck777 in ["999", "888", "666", "555", "444", "333", "222", "111"]:
                wallet += 50
                print(f"You win 50%! New wallet balance: {wallet}")
            else:
                wallet -= 50
                print(f"You lost 50. New wallet balance: {wallet}")

    elif playerchosie == 2:
        print("You have chosen blackjack21 , black jack under coding xd ")
    elif playerchosie == 3:
        emojis = {
            "rock": "🪨",
            "paper": "📄",
            "scissors": "✂️"
        }

        print(f"You have chosen ✂️📄🪨 game ")

        def rps_game():
            playerrps = int(input(f"choose 1: {emojis['rock']}, 2: {emojis['paper']}, 3: {emojis['scissors']}"))
            cpurps = random.randint(1, 3)
            if playerrps == cpurps:
                print("It's a draw")
            elif playerrps == 1 and cpurps == 3 or playerrps == 2 and cpurps == 1 or playerrps == 3 and cpurps == 2:
                print("You won")
                wallet += 100

        rps_game()










    else:
        print("You didn't choose any game")


coregame()
