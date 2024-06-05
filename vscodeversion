import random
from colorama import Fore
import math
from spellchecker import SpellChecker

mycount = 0
compcount = 0
spell = SpellChecker()

# possible moves
moves = ["charge", "fireball", "iceball", "shield", "megaball"]
moves1 = ["charge" , "fireball", "iceball", "shield"]
moves2 = ["charge" , "fireball", "shield"]
moves3 = ["charge" , "shield"]
spell.word_frequency.load_text_file('./fireballmoves.txt')


n = moves3 #computer possible moveset
m = moves3 #player possible moveset
gameStart = ("Game started!")
print(f'\033[32;1m{gameStart}\033[0m')
for i in range(0,100):
    a = input() #player move
    b = random.choice(n) #computer move
    if a == "end":
        exit()
    #legal move
    if a in moves:
        if a not in m:
            print ("not enough charges!")
            exit() 
    #spellcheck
    if a not in moves:
        likely = spell.correction(a)
        print(f"Did you mean {likely}?")
        print("Enter yes or no")
        yesorno = input()
        if yesorno == 'yes':
            if likely in m:
                a = likely
            else:
                print("not enough charges!")
                exit()
        if yesorno == 'no':
            print("Game ending...")
            exit()

    #charge counting
    if a == "fireball": 
        mycount -= 1
    elif a == "iceball":
        mycount -= 2
    if b == "fireball":
        compcount -= 1
    elif b == "iceball":
        compcount -= 2
    if a == "charge":
        mycount += 1
    if b == "charge":
        compcount += 1

    #legal move checker
    if compcount == 0:
        n = moves3
    if compcount == 1:
        n = moves2
    if 2 <= compcount < 5:
        n = moves1
    if compcount >= 5:
        n = moves
    if mycount == 0:
        m = moves3
    if mycount == 1:
        m = moves2
    if 2 <= mycount < 5:
        m = moves1
    if mycount >= 5:
        m = moves

    #prints
    compprint = (f"The Computer chose {b} as their move!")
    youprint = (f"You chose {a} as your move!")
    print(f'\033[94;1m{compprint}\033[0m')
    print(f'\033[94;1m{youprint}\033[0m')
    print(f'\033[36;1m{a}\033[0m',f'\033[31;1m{b}\033[0m',f'\033[36;1m{mycount}\033[0m',f'\033[31;1m{compcount}\033[0m')

    #comp vs player logic
    if a == "shield" and b != "megaball":
        continue
    elif b == "shield" and a != "megaball":
        continue
    elif a == "iceball" and b == "iceball":
        continue
    if a == "megaball" and b == "megaball":
        continue
    elif a == "charge" and b == "fireball" or b == "iceball" or b == "megaball":
        print ("You lost :(")
        exit()
    if a == "fireball" and b == "iceball" or b == "megaball":
        print ("You lost :(")
        exit()
    elif b == "charge" and a == "fireball" or a == "iceball" or a == "megaball":
        print ("You won :)")
        exit()
    if a == "fireball" and b == "charge":
        print ("You won :)")
        exit()
    elif a == "iceball" and b == "charge":
        print ("You won :)")
        exit()
    if b == "fireball" and a == "iceball" or a == "megaball":
        print ("You won :)")
        exit()
    elif b == "megaball" and a != "megaball": 
        print ("You lost")
        exit()     
    elif a == "megaball" and b != "megaball": 
        print ("You won :)")
        exit()
