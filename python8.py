questions = [
    {"q": "What is 5 x 7?",             "a": "35"},
    {"q": "Capital of India?",           "a": "delhi"},
    {"q": "How many days in a week?",    "a": "7"},
    {"q": "What color is the sky?",      "a": "blue"},
    {"q": "Python is a programming ___?","a": "language"},
]

score = 0
print("=== QUIZ GAME ===")
print(f"Answer {len(questions)} questions!\n")

for i, item in enumerate(questions, 1):
    print(f"Q{i}: {item['q']}")
    answer = input("Your answer: ").lower().strip()

    if answer == item["a"]:
        print("Correct! +1 point\n")
        score += 1
    else:
        print(f"Wrong! Answer was: {item['a']}\n")

print(f"=== RESULT ===")
print(f"Score: {score}/{len(questions)}")

if score == len(questions):
    print("PERFECT SCORE!")
elif score >= 3:
    print("Great job!")
else:
    print("Keep practicing!")