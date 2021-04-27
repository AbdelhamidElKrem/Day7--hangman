
import random;
from hangman_logo import stages ;
from hangman_logo import logo;
from hangman_words import word_list
from replit import clear

lives = 6;
random_word = random.choice(word_list);
display = []
end_of_game  = False

print(logo + "\n\n");





for i in range(0,len(random_word)):
  display += "_"


while end_of_game == False :
  a = input("guess a letter:").lower();

  #Use the clear() function imported from replit to clear the output between guesses.
  clear()


  for i in range(len(random_word)):
    letter = random_word[i];
    if a == letter :
      display[i] = a

  print(f"{' '.join(display)}")
  if a not in random_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")
  if "_" not in display:
    end_of_game = True
    print("you win")