import random
import main
from main import health
from main import death
from main import sanity
from main import stats
from random import randrange

WareBeast = 20
Whack = randrange(1, 10)
WareBeast = WareBeast - Whack
print(WareBeast)
if Whack > 9:
    print("Wow a Critical hit!")

while WareBeast <= 0 or health <= 0:
    Wareattack1 = randrange(1, 5)
    health = health - Wareattack1
    print(health)
    attack = randrange(2 - 7)

    if health <= 0:
        print(death)
        # sleep(1)
        exit()
    if WareBeast <= 0:
        print("Good Job you won!")
