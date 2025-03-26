#Shatzee; Made by Adrian Klos
import random
ticket = 30
money = 0
sum = 0
number = 0
s = 0
gs = 0
rounds = 10000

def rollddice():
    global money, s, gs
    pdie = random.randrange(1,7)
    ndie = random.randrange(1,7)
    print("-----")
    print(pdie)
    print(ndie)
    print("--0--")
    print(money)
    if pdie == 6 and ndie == 1:
        print("Shatzee")
        s+=1
    if pdie > ndie:
        a = money
        for i in range (abs(pdie-ndie)):
            money+=rollwdice()
            print(money)
        if money==a+30:
            print("Grand Shatzee!")
            gs+=1
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
    global money, s, gs, ticket, rounds
    for i in range(rounds):
        rollddice()
    print("--00--")
    print(money/rounds)
    print(s)
    print(s/rounds)
    print(gs)
    print(gs/rounds)


main()
