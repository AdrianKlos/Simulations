# Shatzee; Made by Adrian Klos
import random
money = 0
shatzee = 0
grandshatzee = 0
rounds = 10000

def rollddice():
    global money, shatzee, grandshatzee
    pdie = random.randrange(1,7)
    ndie = random.randrange(1,7)
    print("-----")
    print(pdie)
    print(ndie)
    print("--0--")
    print(money)
    if pdie == 6 and ndie == 1:
        print("Shatzee")
        shatzee+=1
    if pdie > ndie:
        a = money
        for i in range (abs(pdie-ndie)):
            money+=rollwdice()
            print(money)
        if money == a+30:
            print("Grand Shatzee!")
            grandshatzee+=1
    if pdie < ndie:
        for i in range (abs(pdie-ndie)):
            money-=rollwdice()
            print(money)
    if pdie == ndie:
        money+=0
        print(money)

def rollwdice():
    print("-----")
    return random.randrange(1,7)

def main():
    global money, shatzee, grandshatzee, rounds
    for i in range(rounds):
        rollddice()
    print("--00--")
    print(money)
    print(money/rounds)
    print(shatzee)
    print(shatzee/rounds)
    print(grandshatzee)
    print(grandshatzee/rounds)


main()
