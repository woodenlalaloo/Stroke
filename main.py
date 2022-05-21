from time import sleep
import random
from random import randrange
# from io import StringIO
import sys

import rand as rand

health = 20
sanity = 20
import cutscene1
from cutscene1 import playername

# sleep(4)
print(
    "Miraculosly your phone isnt destroyed and you can see news reports saying that in the town center a thermo-nuclear weapon was detonated and you are very lucky that you survived."
)
# sleep(5)
print(
    "You relize that your family lived very close to the town center and it sinks in that your family is dead. You hear further explosions around you."
)
# sleep(4)
woundremove1 = input(
    "Type 1 to remove the concrete on your left leg. Type 2 to cover your wound on your right ankle >"
)
if woundremove1 == "1":
    print(
        "You get rid of the concrete slab thats on your leg. Your legs are shattered"
    )
if woundremove1 == "2":
    print(
        "you cover your ankle as you can barely look at it.The bleeding stops."
    )
# sleep(1)
print("Goal: Find some help.")
# sleep(1)
print("A strange man walks over to you that has a well defined jaw.")
# sleep(1.5)
print("As you see him walk over you notice....")
# sleep(3)
print("ITS THE ROCK")
# sleep(2)
print("You: Dwane what happened!?")
# sleep(1.5)
print("The Rock: You dont know?")
# sleep(1.5)
print("You: No?")
# sleep(1.5)
print("The rock: the city exploded bozo")
# sleep(1)
print("You: well I know that..")
# sleep(1)
print("The rock: get up.")
# sleep(1)
print("You get up on a stick of concrete and follow the rock")
# sleep(1)
print("you get in a car and drive out of the city")
# sleep(1)
print("You look to your left and see the rock at the wheel A## sleep!")
# sleep(0.5)
print("You: WAKE UP DWANE!!!!")
# sleep(1.5)
carcrash1 = input(
    "Type 1 to try to control the wheel, type 2 to wake up dwane >")
if carcrash1 == "1":
    print("You try to grab the wheel but it is too late.. ")
if carcrash1 == "2":
    print("You slap dwane as he wakes up. The Rock:huh-AAAAAAAA")
# sleep(1.5)
explosionDamage = randrange(5)
print("A yellow-red explosion goes into your face")
explosionDamage = randrange(5, 8)
# sleep(1.5)
health -= explosionDamage
print("Your health is now " + str(health))
# sleep(1.5)
print("Dwane is crushed to bits.")
# sleep(1.5)
print("He was your only friend.")
stats = "Health: " + str(health) + ",sanity: " + str(
    sanity) + "."
# sleep(1.5)
print("You look at dwane in greif as you cry to yourself")
sanity -= randrange(5, 8)
print("Your sanity is now " + str(sanity) + ".")
# sleep (1.5)
print("You find a flare gun and a utility knife in Dwanes pocket.")
# sleep(1.5)
woundremove2 = input(
    "Type 1 to remove the shrapnel from your hand. Type 2 to cover the wound >"
)
if woundremove2 == "1":
    print("You get rid of the scrap from your hand")
if woundremove2 == "2":
    print("you cover your your hand and scream in pain.")
# sleep(2)
print("You stumble to a shed and open the door")
# sleep(1.5)
search1 = input("Type 1 to look around the shed type 2 to leave the shed. >")
if search1 == "1":
    print("You find bandages and heal.")
    bandages1 = randrange(5, 8)
    health += bandages1
    print("You heal to " + str(health))
    # sleep(1.5)
    sanity += bandages1
    print("Your sanity is" + str(sanity))
if search1 == "2":
    print("You leave the shed.")
# sleep(1.5)
print("you see an other person in the distance")
# sleep(1.5)
print("???:Yes")
# sleep(1.5)
print("You:Hello?")
# sleep(1.5)
print("Tanner:yes.")
# sleep(1.5)
print("Tanner: Yes!!!")
# sleep(1.5)
print("You look to the side and you see someone on a bike")
# sleep(1.5)
print("???: Hey nerd")
# sleep(1.5)
print("Tanner gets shot in the hand")
# sleep(1.5)
print("Tanner YES")
# sleep(1.5)
print("tanner crys then gets shot again")
# sleep(1.5)
print("You: Wait... GABE!?!")
# sleep(1.5)
print("Gabe: Hi " + playername)
# sleep(1.5)
print("You:Why did you kill tanner?!?!")
# sleep(1.5)
print("Gabe: Because i wanted to.")
# sleep(1.5)
print("You: you shouldn't have done that!")
# sleep(1.5)
print("All of the sudden a man walking on all fours like a gorilla runs up")
# sleep(1.5)
print("Monke monk: Chonk monk?")
# the responce partwhat about it you will see
# MONK=input("Type 1 if you want to say 'Chonk Monk' back ")
# from chonkmonk import answered
from chonkmonk import inducted

death = "Game over."
from chonkmonk import *

answered = input(
    "Type 1 to say chonk monk back. Type 2 to say nothing type 3 to run away. > "
).strip()
if int(answered) == 1:
    bool(inducted) == True
    print(
        "the Monke monk grabs you and takes you to his house you get inducted into his cult you live out the rest of "
        "your life a chonk monk and die a sad life married to Monkela and sacrificed to the gods. "
    )
    exec(open("slainDeath.py").read())
if int(answered) == 2:
    bool(monkkilled) == True
    print(
        "The man summons a ball of fire into his hand yells'MONKDOKEN!' and blast you, turning you into nothing more "
        "than ashes on the ground "
    )
    exec(open("slainDeath.py").read())
if int(answered) == 3:
    print(
        "you run away from the man but he gives chase you end up running into an old abandoned warehouse, "
        "but you seem to have lost him "
    )
# sleep(1.5)
print("in the warehouse you see a right and left path ")
# sleep(1.5)
WareChoice = input("Type 1 to go left and 2 to go right. > ").strip()
if int(WareChoice) == 1:
    print(
        "You go to the left suddenly you get the feeling you are being watched and out of nowhere a creature jumps in "
        "front and scares you. lose sanity "
    )
    jumpscare1 = randrange(2, 5)
    sanity = sanity = jumpscare1
    print("Your sanity is now " + str(sanity) + " oh no! BOZO")
if int(WareChoice) == 2:
    print(
        "you go on the right path and on the way you see a hideous beast. You notice it is looking intently at the "
        "left path as if it is expecting someone. you pick a nearby club and whack the creature as hard as you can "
    )
#    from WareBattle import

food = input(print("Type 1 to eat the meat (WARNING chance of food poisoning) type 2 to walk away")).strip()
wareFood = randrange(1,2)
printHeath = "Your health is now " + str(health) + "."
if food == 1:
    print("you eat the meat")
    print(printHeath)
    if wareFood == 1:
        health -= 3
    if wareFood == 2:
        health += 3
    if wareFood == 1:
        print("Aw man! You got food poisoning")
if food == 2:
    print("you walk away and vow never to return")
print("You leave the warehouse and see a path leading to a highway to your right. To your left you see some woods.")

wildernessVentureChoice= input("Type 1 to go to the highway. Type 2 to venture into the woods.")
if wildernessVentureChoice == "1":
  print("You venture into the woods.")
  exec(open("woods.py").read())
if wildernessVentureChoice =="2":
  print("You follow the path and walk onto the highway.")
  exec(open("highway.py").read())

#code here will be moved to highway.py when i get the chance to
print("You are walking on the highway when suddenly you see a truck driving.")
# sleep(3)
print("It's a... walmart truck???")
# sleep(1.5)
print("You quickly take out the flare gun Dwane gave you and as the truck is going by you shoot the driver in the head, instintly killing them.")
# sleep(4)
print("The truck goes off the road and into the ditch where you despose of the body and decide you will live in the truck.")
# sleep(3)
print("You open the back and find that theres lots of food, water, and toys.")
# sleep(2)
print("Most of the toys are not useful but behind all the toys you find something amazing. A crossbow. You can fight people and creatures now.")
# sleep(4)
print("You also find some bandages and wrap them around your laceration.")
# sleep(1.5)
print("You decide to go to sleep")
#end of code that will be added to highway.py
#code here will be moved to woods.py
print("You venture into the woods and find a small 'Fort' that was probably made by some kids.")
# sleep(2)
print("You think to yourself 'It's better then nothing' and sleep the night there.")
# sleep(5)
print("You wake up and start looking around the forest for some kind of food.")
# sleep(3)
print("You find a berry bush.")
pickBerries1 == input("Type 1 to pick the berries. Type 2 to leave them.")
if pickBerries1 == "1":
  print("You pick and eat the berries.")
  berryFoodPoisoning1 == randrange(-5,5)
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
#we cant call main.py anymore or it will restart it so instead make a new file named part2.py or smth and go from there