import random
import time
import playsound
from captcha.image import ImageCaptcha
from PIL import Image

since = str("SINCE OCTOBER 2021")
print("Hello! I am CoreAI, a very simple and user-friendly chatbot.")
time.sleep(1)
print("|| ", since, " ||")
time.sleep(1)
print()
name = input("What can I call you as? - ")
time.sleep(1)
print("Good to meet you,", name, end=".")
time.sleep(1)
print()
print("Just to make sure that you are not a robot, please solve the following CAPTCHA.")
print("NOTE - We will redirect you to a different window where you will see the image. From there you must find out the text and then write your answer here.")
time.sleep(1)
image = ImageCaptcha(width = 280, height = 90)
captcha_textlist = ["xscdvftygbuhn", "yyy324ooo", "scrumdiddlyumptious", "alionsmane", "-altcodes-", "griffpatch-lord", "awesomeyoungcoder"]
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

def main():
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
        print("Type 'tell me a joke' to get a funny joke.")
        print("Type 'version' to get the current version of CoreAI.")
        print("Type 'changelog' to see all the milestones of the making of this program.")
        print("Type 'name' to change your username.")
        print(f"I am still adding more commands, so look out for new releases and versions, {name}!")
        time.sleep(1)
        funchandler(1)
    elif prompt == "version":
        time.sleep(1)
        print("VERSION 0.3.1")
        time.sleep(1)
        funchandler(1)
    elif prompt == "changelog":
        time.sleep(1)
        print()
        print("V0.0.2:")
        print(" - First command of asking name of user")
        print("V0.1.3:")
        print(" - Added CAPTCHA for user verification")
        print(" - Added funcmap and funchandler to reduce program size in future")
        print("V0.2.1:")
        print(" - Added 'hello', 'tell me a joke' and 'command' commands")
        print(" - Added time pause function to smoothen up the program")
        print("V0.3.1:")
        print(" - Added a changelog to mark all milestones in making this program")
        print("V0.4.2:")
        print(" - Added the highlow game")
        print(" - Converted the parameter for funchandler to 'int' to prevent complications")
        print("V0.4.4")
        print(" - Added beta option to play music (still under development)")
        print(" - Added 'name' command to change the user's name")
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
    else:
        print("Didn't get that! Try again.")
        funchandler(1)

def highlow():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    time.sleep(1)
    print(1)
    print("I chose a number between 1 and 100.")
    time.sleep(1)
    print(f"Do you think the number is greater or less than {number2}?")
    time.sleep(1)
    print()
    print("Type '>' if you think it's greater, '<' if it's smaller, '>' if it's greater, and '=' if it's equal.")
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

def musicplayer():
    time.sleep(1)
    print(f"Please enter the entire file path for the file you want to play, {name} (.mp3 or .wav only.)")
    prompt = input(">>> ")
    time.sleep(1)
    playsound.playsound(prompt)
    funchandler(1)

funcmap = {1 : main, 2 : highlow, 3 : musicplayer}

def funchandler(a = int):
    funcmap[a]()

if x == "wrong answer":
    exit
else:
    time.sleep(1)
    print(f"Type 'commands' to view a list of the usable commands with CoreAI, {name}.")
    time.sleep(1)
    funchandler(1)