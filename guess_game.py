from random import randint

print("This is a guess game, pick a number between [1, 10]")
num = randint(1,10)

trial = 0

while True:
    if trial > 0:
        guess = input("Pick again: ")
        if num == int(guess, base=10):
            print("You are a genius")
            break
        else:
            print("You are wrong guess again")
    else:
        guess = input("Welcome, pick from [1,10]: ")
        if num == int(guess, base=10):
            print("You are a genius")
            break
        else:
            print("You are wrong guess again")
    trial = 1