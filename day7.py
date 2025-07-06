import random
import os
os.system('cls' )

word_list = [
    "apple", "river", "cloud", "stone", "light", "dream", "forest", "music", "dance", "flame",
    "echo", "storm", "peace", "truth", "magic", "grace", "smile", "laugh", "hope", "shine",
    "breeze", "leaf", "sky", "ocean", "wave", "dust", "spark", "glow", "whisper", "shadow",
    "mirror", "path", "heart", "soul", "wish", "rain", "snow", "wind", "fire", "ice",
    "gold", "silver", "stone", "petal", "root", "branch", "seed", "fruit", "sun", "moon"
]

word = random.choice(word_list)
print(word)  # For debugging purposes, you can see the chosen word
display = "_ " * len(word)
print(display)
guessesletter = []
life=7 
while life > 1:
    while "_" in display:
        
        display  = " "
        guesses = input("Guess a letter: ")
        guessesletter.append(guesses.lower())
        if guesses.lower() in word:
            print("Correct!")   
        else:
            life -= 1
            if life == 6:
                print("""
   +----+
   |    |   
   |    O   
   |   
   |   
        

""")
            elif life == 5:
                print("""
   +----+
   |    |   
   |    O   
   |    |
   |   
""")
            elif life == 4:
                print("""
   +----+
   |    |   
   |    O   
   |   /|
   |   
""")
            elif life == 3:
                print("""
   +----+
   |    |   
   |    O   
   |   /|\ 
   |   
""")
            elif life == 2:
                print("""
  +----+
   |    |   
   |    O   
   |   /|\ 
   |   / 
""")
            elif life == 1:
                print("""
   +----+
   |    |   
   |    O   
   |   /|\
   |   / \
""")
                print("Game Over! The word was:", word)

        
        for letter in word:
            if letter in guessesletter:
                # If the guessed letter is in the word, display it
                display += letter
            else:


                display += "_"

        print (display)
        if "_" not in display:
            print("Congratulations! You've guessed the word:", word)
        