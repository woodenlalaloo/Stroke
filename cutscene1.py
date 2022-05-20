from time import sleep
import random
from random import randrange
from io import StringIO
import sys

health = 20
sanity = 20

# while True:
##sleep(90- time() % 90)
# print("Health: "+str(health)+", sanity: "+str(sanity)+")
playername = input("Type your name to begin. > ")

print("Hi " + playername + "!")
print("Your stats are as follows. Health, and sanity are both 20. If health reaches 0 then you die. Sanity can go as "
      "low as -20 but if it gets to there you instantly die.")
# sleep (1.5)

print("You are about to have a stroke.")
# sleep(2)
print("3")
# sleep(1)
print("2")
# sleep(1)
print("1...")
# sleep(5)
print("Doctor: Hello " + playername + "?")
# sleep(1.25)
print("Doctor: " + playername + " wake up!")
# sleep(1.5)
print("You sit up on a hospital bed as your vision clears...")
# sleep(1.75)
print("Doctor: " + playername + " you had a stroke!")
# sleep(1.75)
print("Doctor: You were lucky you were found quickly.")
responce1 = input("Type 1 to ask if you are ok. Type 2 to ask how you were found. > ")
if responce1 < "1":
    print("Type something else.")
    responce1 = input("Type 1 to ask if you are ok. Type 2 to ask how you were found. > ")
if responce1 > "2":
    print("Type something else.")
    responce1 = input("Type 1 to ask if you are ok. Type 2 to ask how you were found. > ")
if responce1 == "1":
    print("Doctor: You suffered minor brain damage and heart failiure.")
if responce1 == "2":
    print(
        "Doctor: Well you were at Russells Convenience Store when you collapsed. People rushed to see what the noise "
        "was and after seeing you collapsed on the ground called 911.")
# sleep(2.5)
print("Doctor: We are going to do some blood tests and then some physical therapy if needed.")
# sleep(1)
print("You: Ok.")
# sleep(1)
print("You decide to go back to #sleep.")
# sleep(3)
print("You wake up.")
# sleep(1.5)
print("Doctor: You are all good and are going to be discharged in a half hour.")
# sleep(3)
print("It is 30 minutes later.")
# sleep(1.5)
print("The doctor walks in.")
# sleep(1)
print("Doctor: Ok you can stand up and follow me.")
# sleep(1.5)
print("You follow the doctor.")
# sleep(3)
print("Doctor: Ok you are all set! Come back if there are any issues.")
# sleep(1.75)
responce2 = input("Type 1 to call an uber. Type 2 to call a family member to come pick you up. > ")
if responce2 < "1":
    print("Type something else.")
    responce2 = input("Type 1 to call an uber. Type 2 to call a family member to come pick you up. > ")
if responce2 > "2":
    print("Type something else.")
    responce2 = input("Type 1 to call an uber. Type 2 to call a family member to come pick you up. > ")
if responce2 == "1":
    print("An uber is on its way.")
if responce2 == "2":
    print("You call your brother and he says he will be there in 10.")
# sleep(2)
print(
    "You are sitting in the bench next to the door when suddenly a flash of light blinds you and you hear crumbling "
    "and a ringing in your ear.")
# sleep(5)
print(" ")
print("You wake up with your legs crushed.")
# sleep (1.75)
print("You look up and the hospital is gone.")
# sleep(1.75)
print(
    "You look down at your feet and see a pool of blood around it and one of your legs is crushed by a heavy piece of "
    "concrete. A black rain starts.")
# sleep(5)
print("You don't know what's happened to you or why.")
exec(open("main.py").read())
