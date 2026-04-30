import random

# Word list
words = ["python", "hangman", "computer", "keyboard", "program"]
word = random.choice(words)

guessed = []
lives = 6

print("=== HANGMAN ===")
print(f"Word has {len(word)} letters\n")

while lives > 0:
    # Display current word state
    display = " ".join([l if l in guessed else "_" for l in word])
    print(f"Word: {display}")
    print(f"Lives: {'* ' * lives}")
    print(f"Guessed: {', '.join(guessed) if guessed else 'none'}\n")

    # Check win condition early
    if "_" not in display:
        print(f"🎉 YOU WIN! The word was: {word}")
        break

    # Take input
    letter = input("Guess a letter: ").lower()

    # Validate input
    if not letter.isalpha() or len(letter) != 1:
        print("Enter a single valid letter!\n")
        continue

    if letter in guessed:
        print("Already guessed that!\n")
        continue

    guessed.append(letter)

    # Check guess
    if letter in word:
        print("Correct!\n")
    else:
        lives -= 1
        print("Wrong! -1 life\n")

# If loop ends without break → game over
if lives == 0:
    print(f"💀 GAME OVER! The word was: {word}")