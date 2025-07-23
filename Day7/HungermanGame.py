import random
print("                                                                                                                ")
print("********************************HungerMan********************************************** ")
hangmanPic = [
    '''
  +---+
  |   |
  O   |
 /|\  |  
 / \  |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
      |
      |
      |
      |
========='''
]
#### Total Lives We have
lives=6
print(f"\nYou have Total lives:{lives}")
### randow wonrds generation
Words=["marwat","malkova","rajpot"]
randomWords=random.choice(Words)
###print(randomWords)
##finding length for making placeholders
wordLength=len(randomWords)
placholder=""
for i in range(wordLength):
    placholder+="_"
print(placholder)
print(hangmanPic[6])




##For Running While Loop we create a boolean variable
game_over=False
###For storing guess while each iteration of while loop
correct_letters=[]

while not game_over:
    guess=input("Guess a Letter: ").lower()     #### .lower to covert it into small cases

    display=""                                  ##### to display the message like a_i_f

    for letter in randomWords:

        if letter==guess:                      ###### if guess letter is in random word
            display+=letter  
            correct_letters.append(guess)      ###### appending guess to correct letter list to store in memory
            

        elif letter in correct_letters:        ###### adding letters in list from list to string 
            display+=letter

        else:                                 ######  if guess not match simply  add "_" in display
            display+="_"
         

    if guess not in randomWords:            ########## if the guess is not in random words simply minus 1 from lives and if lives become 0 you will lose the game 
        lives-=1
        print(f"\nlives Remaining:{lives}")
        if lives==0:
            game_over=True
            print("******************        you Lose :(        **************** ")
            

  
    print(display)                     ######### printing the dispplay variable having what scenarios are now on running like         a__k_cc_
    if "_" not in display:
        game_over=True
        print("******************         You win ,You Save Live  :)       ************************")
    print(hangmanPic[lives])           ########## shows the asscii art of hangman according to lives
        








