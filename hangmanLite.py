import random

myWord = ("Eat", "Play", "Enjoy", "Right", "Live", "Home", "Vacation", "Persistent", "Jungle", "Space")
randMovie = random.randint(0, 9)
randMovie = myWord[randMovie]

print(str(len(randMovie)) + " letters long ")
tries = 5;
while tries > 0:
    randLet = input("Guess a letter. ")
    if randLet.lower() in randMovie.lower():
        print("Congratulations! You are correct. ")
    else:
        print("Sorry, you guessed wrong! Try again. ")
    tries -= 1

finalTry = input("Guess the entire word. ")
print(finalTry.lower() == randMovie.lower())
print(randMovie + " was the word ")
