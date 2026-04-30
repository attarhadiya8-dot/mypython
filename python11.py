import random
import time

print("=== MEMORY GAME ===")
print("Remember the numbers, then type them back!\n")

score = 0

for level in range(1, 6):             # 5 levels
    count = level + 2                 # level 1 = 3 numbers, level 5 = 7 numbers
    numbers = [random.randint(1, 9) for _ in range(count)]

    print(f"Level {level} — Remember {count} numbers:")
    print(" ".join(str(n) for n in numbers))
    time.sleep(2)                     # show for 2 seconds
    print("\n" * 20)                  # clear screen effect

    answer = input("Type the numbers (space separated): ")
    typed = list(map(int, answer.split()))

    if typed == numbers:
        print("Correct! Moving up!\n")
        score += 1
    else:
        print(f"Wrong! It was: {' '.join(map(str, numbers))}\n")
        print(f"Final score: {score}/5")
        break
else:
    print(f"YOU COMPLETED ALL LEVELS! Score: {score}/5")