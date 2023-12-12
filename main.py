
import random
mycount = 0
compcount = 0

# possible moves
moves = ["charge", "fireball", "iceball", "shield", "megaball"]
moves1 = ["charge" , "fireball", "iceball", "shield"]
moves2 = ["charge" , "fireball", "shield"]
moves3 = ["charge" , "shield"]

n = moves3
m = moves3

for i in range(0,20):
    a = input()
    b = random.choice(n)
    if a == "charge":
        mycount += 1
    if b == "charge":
        compcount += 1
    if compcount == 0:
        n = moves3
    if compcount >= 1:
        n = moves2
    if compcount >= 2:
        n = moves1
    if compcount >= 5:
        n = moves
    if mycount == 0:
        m = moves3
    if mycount >= 1:
        m = moves2
    if mycount >= 2:
        m = moves1
    if mycount >= 5:
        m = moves
    if mycount <= 0 and a != "shield":
        print ("error you cannot do that")
        exit()
    print(a, b, mycount, compcount)
    #exit()
    print ("The Computer chose " + b + " as their move!")
    print ("You chose " + a + " as your move!")
    
    if a not in m:
        print ("error")
        exit() 
    if a == "fireball":
        mycount -= 1
    elif a == "iceball":
        mycount -= 2
    if b == "fireball":
        compcount -= 1
    elif b == "iceball":
        compcount -= 2
 

    if a == "shield" and b != "megaball":
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
        
    
