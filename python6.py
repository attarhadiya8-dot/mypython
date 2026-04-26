
import random
secret = random.randint(1, 1000)  # Pick a random number
attempts = 0
while True:               # Keep looping forever...
    guess = int(input("Guess (1-1000): "))
    attempts += 1

    if guess < secret:
        print("Too low! ⬆️")
    elif guess > secret:
        print("Too high! ⬇️")
    else:
        print(f"🎉 Correct in {attempts} tries!")
        break             # ...until we BREAK out