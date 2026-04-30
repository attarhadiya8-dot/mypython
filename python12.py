import random

words = ["python", "variable", "function", "loop", "string",
         "integer", "boolean", "program", "keyboard", "screen"]

score = 0
total = 5

print("=== WORD SCRAMBLE ===")
print(f"Unscramble {total} words!\n")

used = []
for round_num in range(1, total + 1):
    # Pick unused word
    word = random.choice([w for w in words if w not in used])
    used.append(word)

    # Scramble it
    letters = list(word)
    while letters == list(word):      # keep scrambling until different
        random.shuffle(letters)
    scrambled = "".join(letters)

    print(f"Round {round_num}: {scrambled.upper()}")

    attempts = 3
    won = False

    while attempts > 0:
        guess = input(f"Unscramble it ({attempts} tries left): ").lower()
        if guess == word:
            print(f"Correct! The word was '{word}'\n")
            score += 1
            won = True
            break
        else:
            attempts -= 1
            if attempts > 0:
                print("Wrong, try again!")
            else:
                print(f"Out of tries! Answer was: '{word}'\n")

print(f"=== DONE! Score: {score}/{total} ===")