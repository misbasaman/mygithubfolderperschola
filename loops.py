import random
print("welcome to guess the number!")
print("the rules are simple. I will think of a number and you will guess it")
number = random.randint(1,10)
isguessright = False

while isguessright != True:
    guess=input("Guess a number between 1 - 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isguessright = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

for x in range (0, 11):
    print(x)