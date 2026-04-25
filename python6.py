import random
secret = random.randint(1,10)
attempts =0

while true:
  guess=int(input("Guess a random number from 1 to 10 :"))
  attempts +=1

  if guess < secret:
    print("its too low!!")
  elif guess > secret:
    print("its too high")
  else:
    print(f"Correct guess in {attempts} tries!!")
    break
    
