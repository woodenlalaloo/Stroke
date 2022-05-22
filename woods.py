#code here will be moved to woods.py
from main import health
from main import printHealth
from random import randrange
from clear import clear
clear()
print("You venture into the woods and find a small 'Fort' that was probably made by some kids.")
# sleep(2)
print("You think to yourself 'It's better then nothing' and sleep the night there.")
# sleep(5)
print("You wake up and start looking around the forest for some kind of food.")
# sleep(3)
print("You find a berry bush.")
pickBerries1 = input("Type 1 to pick the berries. Type 2 to leave them.")
if pickBerries1 == "1":
  print("You pick and eat the berries.")
  berryFoodPoisoning1 = randrange(-5,5)
  if berryFoodPoisoning1 >= -1:
    print("Oh no, you got food poisoning. You proceed to vomit the contents of your stomach.")
    # sleep(2)
  health += berryFoodPoisoning1
  print(printHealth)
if pickBerries1 == "2":
  print("You leave the berries.")

# sleep(3)
print("You find a long, sturdy stick and use the utility knife Dwane had to turn it into a spear.")
# sleep(2)
print("You move around the forest, looking for something to kill. You almost got some squirells but you missed.")
# sleep(2)
print("After a day with no luck you go to sleep.")
# sleep(5)
print("You wake up in the morning and start hunting again. Eventualy you find a deer and start sneaking up to it. Suddenly its ears perk up. It spins around and sees you. It's hair is sticking up and it's ears are back.")
# sleep(5)
print("You know you read somewhere that means that it's scared. Then, out of the blue, it charges straight at you and throws you off of the cliff. Time seems to slow down")
# sleep(2)
print("You think to yourself: Why did I even try. What was the point.")
print(1.5)
print("You plummet to the forest floor where you black out.")
# sleep(6)
print("You come to your senses and find out that you cant move. You try to get up, nothing. You try to move your fingers, nothing.")
# sleep(3)
print("You realize you must have broken your neck and are paralized.")
# sleep(1.5)
print("Just lying down on the dirt, soon bugs and other insects start to suck your blood.")
# sleep(2)
print("You die a slow, painful death, away from family or friends.")
exec(open("starveDeath.py").read())
#end of code to add to woods.py


