from random import choice

objects = ["rock", "paper", "scissors"]
computer = choice(objects)
rps = input("what will you choose? Rock, Paper or scissors?").lower().strip()
if rps == computer:
    print("it is a tie bruh! No one gets point tbh")
if rps == ("rock"):
    if computer == ("scissors"):
        print("yay! you won! you get a point")
if rps == ("paper"):
    if computer == ("rock"):
        print("yay! you won! you get a point")
if rps == ("scissors"):
    if computer == ("paper"):
        print("yay! you won you get a point")
if computer == ("scissors"):
    if rps == ("paper"):
        print("Noo you lost I get a point")
if computer == ("paper"):
    if rps == ("rock"):
        print("Noo you lost I get a point")
if computer == ("rock"):
    if rps == ("scissors"):
        print("Noo you lost I get a point")
print("Thanks for playing!")
