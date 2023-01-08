import random
import time
import sys
from playsound import playsound
from captcha.image import ImageCaptcha
from PIL import Image

def main(name):
    prompt = input(">>> ")
    if prompt == "hello":
        time.sleep(1)
        print(f"A warm hello to you too, {name}!")
        time.sleep(1)
        funchandler(1)
    elif prompt == "tell me a joke":
        time.sleep(1)
        jokes = ["What type of camera is built in your hand? A HANDY-CAM!!!"]
        jokes.append("Why should computers never be booted? Because it's rude to kick them.")
        jokes.append("How do you throw a space party? You planet.")
        jokes.append("What did the triangle say to the circle? 'You're pointless.'")
        randjoke = random.randint(0, len(jokes)-1)
        print(jokes[randjoke])
        time.sleep(1)
        funchandler(1)
    elif prompt == "commands":
        time.sleep(1)
        print(f"""
Type 'tell me a joke' to get a funny joke.
Type 'version' to get the current version of CoreAI.
Type 'changelog' to see all the milestones of the making of this program.
Type 'name' to change your username.
Type 'play a song' to play any local music files.
Type 'tictactoe' to play a two-player local game of the classic Tic-Tac-Toe.
I am still adding more commands, so look out for new releases and versions, {name}!
        """)
        time.sleep(1)
        funchandler(1)
    elif prompt == "version":
        time.sleep(1)
        print("Current client version of CoreAI : V0.1.6")
        time.sleep(1)
        funchandler(1)
    elif prompt == "changelog":
        time.sleep(1)
        print()
        print("""
Patch 0.1.0:
 - First command of asking name of user
Patch 0.1.1:
- Added CAPTCHA for user verification
- Added funcmap and funchandler to reduce program size in future
Patch 0.1.2:
 - Added 'hello', 'tell me a joke' and 'command' commands
 - Added time pause function to smoothen up the program
Patch 0.1.3:
 - Added a changelog to mark all milestones in making this program
 - Added a version command to view the current client version of CoreAI.
Patch 0.1.4:
 - Added the highlow game
 - Converted the parameter for funchandler to 'int' to prevent complications
Patch 0.1.5:
 - Added 'musicplayer' to play local .mp3 files
 - Added 'name' command to change the user's name
Patch 0.1.6:
 - Fixed the music player
 - Added a local Tic-Tac-Toe game
        """)
        time.sleep(1)
        funchandler(1)
    elif prompt == "start highlow" or prompt == "highlow":
        time.sleep(1)
        print("Loading highlow game...")
        time.sleep(1)
        funchandler(2)
    elif prompt == "play a song" or prompt == "song":
        time.sleep(1)
        funchandler(3)
    elif prompt == "change name" or prompt == "name":
        time.sleep(1)
        namechange = input(f"Enter your new name, {name}: ")
        time.sleep(1)
        print(f"Your name has been changed from {name} to {namechange}")
        name = namechange
        time.sleep(1)
        funchandler(1)
    elif prompt == "tictactoe" or prompt == "play tictactoe":
        time.sleep(1)
        print()
        funchandler(4)
    else:
        print("Didn't get that! Try again.")
        funchandler(1)

def highlow(name):
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    time.sleep(1)
    print()
    print("I chose a number between 1 and 100.")
    time.sleep(1)
    print(f"Do you think the number is greater or less than {number2}?")
    time.sleep(1)
    print()
    print("Type '>' if you think it's greater, '<' if it's smaller, and '=' if it's equal.")
    time.sleep(1)
    print()
    prompt = input(">>> ")
    print()
    if number1 > number2:
        result = ">"
    elif number1 < number2:
        result = "<"
    else:
        result = "="
        time.sleep(1)
    if prompt == result:
        print(f"You win, {name}! The number was {number1}.")
    else:
        print(f"Wrong! The number was {number1}.")
    time.sleep(1)
    print()
    print(f"Do you want to play again, {name}? (yes/no)")
    prompt = input(">>> ")
    if prompt == "yes":
        time.sleep(1)
        print("Okay, rematch!")
        time.sleep(1)
        funchandler(2)
    else:
        time.sleep(1)
        funchandler(1)

def musicplayer(name):
    time.sleep(1)
    print(f"Please enter the entire file path for the file you want to play, {name} (.mp3 or .wav only.)")
    prompt = input(">>> ")
    time.sleep(1)
    playsound(prompt)
    funchandler(1)

def tictactoe_pl1():
    p1 = int(input("Player 1 - Type position >>> "))
    p1 -= 1
    if tictactoe_pos[p1] != '-':
        print("Looks like that square's already been filled. Try again.")
        tictactoe_pl1()
    else:
        tictactoe_pos[p1] = "X"

def tictactoe_pl2():
    p2 = int(input("Player 2 - Type position >>> "))
    p2 -= 1
    if tictactoe_pos[p2] != '-':
        print("Looks like that square's already been filled. Try again.")
        tictactoe_pl2()
    else:
        tictactoe_pos[p2] = "O"

def tictactoe_draw():
    if tictactoe_pos[0] != '-':
        if tictactoe_pos[1] != '-':
            if tictactoe_pos[2] != '-':
                if tictactoe_pos[3] != '-':
                    if tictactoe_pos[4] != '-':
                        if tictactoe_pos[5] != '-':
                            if tictactoe_pos[6] != '-':
                                if tictactoe_pos[7] != '-':
                                    if tictactoe_pos[8] != '-':
                                        print("GG, its a draw!")
                                        funchandler(1)

def tictactoe_board():
    print()
    tictactoe_pl1()
    print()
    print(f"{tictactoe_pos[0]} | {tictactoe_pos[1]} | {tictactoe_pos[2]}")
    print(f"{tictactoe_pos[3]} | {tictactoe_pos[4]} | {tictactoe_pos[5]}")
    print(f"{tictactoe_pos[6]} | {tictactoe_pos[7]} | {tictactoe_pos[8]}")
    if tictactoe_pos[0] == tictactoe_pos[1] == tictactoe_pos[2] == "X":
        print("Player 1 wins!")
        funchandler(1)
    elif tictactoe_pos[3] == tictactoe_pos[4] == tictactoe_pos[5] == "X":
        print("Player 1 wins!")
        funchandler(1)
    elif tictactoe_pos[6] == tictactoe_pos[7] == tictactoe_pos[8] == "X":
        print("Player 1 wins!")
        funchandler(1)
    elif tictactoe_pos[0] == tictactoe_pos[3] == tictactoe_pos[6] == "X":
        print("Player 1 wins!")
        funchandler(1)
    elif tictactoe_pos[1] == tictactoe_pos[4] == tictactoe_pos[7] == "X":
        print("Player 1 wins!")
        funchandler(1)
    elif tictactoe_pos[2] == tictactoe_pos[5] == tictactoe_pos[8] == "X":
        print("Player 1 wins!")
        funchandler(1)
    elif tictactoe_pos[0] == tictactoe_pos[4] == tictactoe_pos[8] == "X":
        print("Player 1 wins!")
        funchandler(1)
    elif tictactoe_pos[2] == tictactoe_pos[4] == tictactoe_pos[6] == "X":
        print("Player 1 wins!")
        funchandler(1)
    tictactoe_draw()
    print()
    tictactoe_pl2()
    print()
    print(f"{tictactoe_pos[0]} | {tictactoe_pos[1]} | {tictactoe_pos[2]}")
    print(f"{tictactoe_pos[3]} | {tictactoe_pos[4]} | {tictactoe_pos[5]}")
    print(f"{tictactoe_pos[6]} | {tictactoe_pos[7]} | {tictactoe_pos[8]}")
    if tictactoe_pos[0] == tictactoe_pos[1] == tictactoe_pos[2] == "X":
        print("Player 2 wins!")
        funchandler(1)
    elif tictactoe_pos[3] == tictactoe_pos[4] == tictactoe_pos[5] == "O":
        print("Player 2 wins!")
        funchandler(1)
    elif tictactoe_pos[6] == tictactoe_pos[7] == tictactoe_pos[8] == "O":
        print("Player 2 wins!")
        funchandler(1)
    elif tictactoe_pos[0] == tictactoe_pos[3] == tictactoe_pos[6] == "O":
        print("Player 2 wins!")
        funchandler(1)
    elif tictactoe_pos[1] == tictactoe_pos[4] == tictactoe_pos[7] == "O":
        print("Player 2 wins!")
        funchandler(1)
    elif tictactoe_pos[2] == tictactoe_pos[5] == tictactoe_pos[8] == "O":
        print("Player 2 wins!")
        funchandler(1)
    elif tictactoe_pos[0] == tictactoe_pos[4] == tictactoe_pos[8] == "O":
        print("Player 2 wins!")
        funchandler(1)
    elif tictactoe_pos[2] == tictactoe_pos[4] == tictactoe_pos[6] == "O":
        print("Player 2 wins!")
        funchandler(1)
    tictactoe_draw()

def tictactoe_main(name):
    global tictactoe_pos
    tictactoe_pos = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    print(f"{tictactoe_pos[0]} | {tictactoe_pos[1]} | {tictactoe_pos[2]}")
    print(f"{tictactoe_pos[3]} | {tictactoe_pos[4]} | {tictactoe_pos[5]}")
    print(f"{tictactoe_pos[6]} | {tictactoe_pos[7]} | {tictactoe_pos[8]}")
    while True:
        tictactoe_board() 

funcmap = {1 : main, 2 : highlow, 3 : musicplayer, 4 : tictactoe_main}

def funchandler(a = int):
    funcmap[a](name)
    
since = str("SINCE OCTOBER 2021")
print("Hello! I am CoreAI, a very simple and user-friendly chatbot.")
time.sleep(1)
print()
name = input("What can I call you as? - ")
time.sleep(1)
print("Nice to meet you,", name, end=".")
time.sleep(1)
print()
print("Just to make sure that you are not a robot, please solve the following CAPTCHA.")
print("NOTE - We will redirect you to a different window where you will see the image. From there you must find out the text and then write your answer here.")
time.sleep(1)
image = ImageCaptcha(width = 700, height = 300)
captcha_textlist = ["xscdvftygbuhn", "yyy324ooo", "bigsHAQ", "scrumdiddlyumptious", "alionsmane", "-altcodes-", "griffpatch-lord", "awesomeyoungcoder", "slimShaDY-BoOm", "snooPIE77"]
randnum = random.randint(0, 6)
captcha = captcha_textlist[randnum]
captcha_data = image.generate(captcha)
image.write(captcha, 'CAPTCHA.png')
img = Image.open('CAPTCHA.png')
img.show()
ans = input("Answer here >>> ")
time.sleep(1)
if ans == captcha :
    print("Correct ✅")
    x = "correct answer"
else:
    print("WRONG ❎. LOOKS LIKE YOU CAN'T ACCESS ME. GOODBYE.")
    x = "wrong answer"
    exit

if x == "wrong answer":
    exit
else:
    time.sleep(1)
    print(f"Type 'commands' to view a list of the usable commands with CoreAI, {name}.")
    time.sleep(1)
    print()
    funchandler(1)