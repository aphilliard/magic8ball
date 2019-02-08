import random
import sys

answers = ("It is certain", "It is decidedly so", "Yes", "Reply hazy try again", "Ask again later", "Concentrate and ask again", "My reply is no", "Outlook not so good", "Very doubtful")

while True:
   user_reply = input("HIT ANY KEY TO Shake the Magic 8-Ball! ('q' to QUIT)")
   if user_reply == "q":
      raise SystemExit
   print(random.choice(answers))