import random
from replit import clear

list = ["test", "word"]

answer = list[random.randint(0, len(list)-1)]
display = []
attempts = 7
wrong = {}

for i in answer:
  if i == " ":
    display.append(" ")
  else:
    display.append("_")
    
def showDisplay():
  print ("".join(display))
  print("Attempts:", attempts)
  print ("Wrong:", ",".join(wrong))


def check_word(guess):
  global display, wrong, attempts
  # check word
  if len(guess) > 1:
    for i in range(len(guess)):
      if guess[i] not in answer and guess[i] not in wrong:
        wrong[guess[i]] = 1
        attempts -= 1
      elif guess[i] in answer:
        for j in range(len(answer)):
          if answer[j] == guess[i]:
            display[j] = guess[i]
  else: 
    found = False
    for i in range(len(answer)):
      if guess == answer[i]:
        display[i] = guess
        found = True
    if not found:
      wrong[guess] = 1
      attempts -= 1
  if "".join(display) == answer and attempts > 0:
    return 1
  else:
    return -1
    
    


while True:
  showDisplay()
  
  guess = input("Enter your guess: ")
  if check_word(guess) == 1:
    print("You win")
    break
  if attempts <= 0:
    print("Fail")
    break
  clear()