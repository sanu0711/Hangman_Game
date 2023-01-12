stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _   _                                          
| | | |                                         
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_| |/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| | | |
                    __/ |                      
                   |___/    '''

                                                         
word_list = ["guava","almond","lemon","watermelon","orange","peach","pear","avocado","kivi",
              "quince","papaya","apple","strawberry","mango","banana","cabbage","tomato","cauliflower",
              "potato","pumpkin","turnip","onion","chilli","carrot","pea","radisdh"]


import random


print("----------------------------------------------------------------------------")
print(f"\t\t{logo}")
print("----------------------------------------------------------------------------")

game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)


display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    print(f"{' '.join(display)}".center(70))
    guess = input("\nGuess the letter : ").lower()


    if guess in display:
        print(f"You have gussed char  already !")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    

    if guess not in chosen_word:
        print(f"You guessed {guess} is wrong ! You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("----------------------------------------------------------------------------")
            print("\t\t\t      You lose ! ")
            print(f"\t\t\tThe word is : {chosen_word}")

            print("----------------------------------------------------------------------------")
    
    if not '_' in display:
        game_is_finished = True
        print("----------------------------------------------------------------------------")
        print("\t\t\t    You win ! ")
        print(f"\t\t\tThe word is : {chosen_word}")
        print("----------------------------------------------------------------------------")

    print(stages[lives])