from hangman_art import stages, logo
from hard_words import word_list
from replit import clear
import random

print(logo) #Styling

#Setup
word = random.choice(word_list)
answer = list(word) #use lists rather than immutable strings
blunders = 0 #used as index in list of ascii art
letters_left = len(answer) #used to check if player won
max_guesses = len(stages) - 1 # 6 chances until hung
guessed_letters = [] #optional track guessed letters bc bug

#Generate blanks
reveal = [] 
for i in range(0, len(answer)):
  reveal.append('_ ')

#Testing code
print(f'Pssst, the solution is {word}.')

#Continue playing as long as have guesses left and not won
while blunders < max_guesses and letters_left != 0:

  #print art and solicit guess
  print(stages[blunders])
  print(f"\n {''.join(reveal)} \n")
  print(f'You have {max_guesses - blunders} chances to guess the word.')

  guess = input("Guess a single letter:\n")

  #optional error handling if typing more than one character
  while len(guess) != 1:
    guess = input("Guess a *single* letter:\n")


  clear() # clears console
  #check if answer contains guess
  if guess not in answer:
    blunders += 1 
    print(f'You guessed {guess}. You chose .... poorly') #Indiana Jones reference
  else:
    print('You guessed right!')
    for i in range(0, len(answer)):
      if guess == answer[i]:
        letters_left -= 1
        reveal[i] = guess + ' ' #fill in blanks
  

# Exited while loop
if blunders == max_guesses:
  print('No more guesses left. You lose')
  print(stages[blunders])
else:
  print(f'Congratulations! The word was "{word}". You win!')