# Rabbit-Wolf Simulation; Made by Adrian Klos
import random

years = 100  # years
grass = 1000  # sq m
rabbit = []  # energy
rabbitage = []
wolf = []
wolfage = []
num_rabbits = []
num_wolves = []
num_grass = []


def rabbitwolfsim():
    global grass, rabbit, rabbitage, wolf, wolfage, years, num_rabbits, num_wolves, num_grass
    grass = 1000  # sq m
    rabbit = []  # energy
    rabbitage = []
    wolf = []
    wolfage = []
    num_rabbits = []
    num_wolves = []
    num_grass = []
    for x in range(10):
        rabbit.append(10)
        rabbitage.append(0)
    for x in range(2):
        wolf.append(50)
        wolfage.append(0)
    years = years
    for x in range(years):

        p = 0.000171 * len(rabbit) * 365  # 171 sq mm of grass eaten per day per rabbit
        grass += 0.1111 * 365
        # 9 days for grass to fully replenish

        if grass > 1000:
            grass = 1000

        # average forest size is 1 sq km
        i = -1
        for y in rabbit:
            i += 1
            rabbitage[i] += 1
            rabbit[i] -= 0.025 * 365  # livecost

            if grass >= 0.000171 * 365:
                grass -= 0.000171 * 365  # eat
                rabbit[i] += 2 * 365

            if y < 0:
                rabbit.pop(i)  # die of hunger
                rabbitage.pop(i)
                i -= 1
            if y >= 7 and len(rabbit) >= 2:
                if len(rabbit) >= 8:
                    z = random.randrange(0, round(len(rabbit) / 5, 0))
                else:
                    z = random.randrange(0, 2)
                if z == 0:
                    rabbit.append(10)  # mate
                    rabbitage.append(0)
            if len(wolf) <= 0:
                print("The wolves went extinct.")
            else:
                c = random.randrange(0, round((len(rabbit) / len(wolf))) + 2)  # chance of chase
                if c == 0:
                    if len(wolf) > 0:
                        f = len(wolf)
                        if f < 1:
                            r = random.randrange(0, f - 1)
                        else:
                            r = 0
                        if ((rabbit[i]) * 5 >= wolf[r]):
                            rabbit[i] -= (wolf[r] / 25) * 365
                        else:
                            wolf[r] += rabbit[i]
                            rabbit.pop(i)  # die from wolf/wolf eat
                            rabbitage.pop(i)
                            i -= 1
            if rabbitage[i] >= 7:  # die of old age
                z = random.randrange(0, 3)
                if z == 0:
                    rabbit.pop(i)  # die
                    rabbitage.pop(i)
                    i -= 1
            if rabbit[i] > 10:
                rabbit[i] = 10
            if rabbit[i] < 0:
                rabbit.pop(i)  # die of hunger
                rabbitage.pop(i)
                i -= 1

        q = -1
        for v in wolf:
            if len(wolf) > 0:
                q += 1
                wolfage[q] += 1

                wolf[q] -= 0.05 * 365  # livecost

                if v < 0:
                    wolf.pop(q)  # die of hunger
                    wolfage.pop(q)

                if q < 0:
                    q = 0
                if v >= 7 and len(wolf) >= 2:
                    if len(wolf) >= 15:
                        z = random.randrange(0, round(len(wolf) / 10, 0))
                    else:
                        z = random.randrange(0, 2)
                    if z == 0:
                        wolf.append(50)  # mate
                        wolfage.append(0)
                if q < 0:
                    q = 0
                if q > len(wolf):
                    q = len(wolf) - 1
                if wolfage[q] >= 8:  # die of old age
                    z = random.randrange(0, 4)
                    if z == 0:
                        wolf.pop(q)  # die
                        wolfage.pop(q)

                if v < 0:
                    wolf.pop(q)  # die of hunger
                    wolfage.pop(q)
            else:
                print("The wolves went extinct.")
            if wolf[q] > 50:
                wolf[q] = 50
            if v < 0:
                wolf.pop(q)  # die of hunger
                wolfage.pop(q)
                q -= 1

        print("Year", x + 1, "Data:")
        t = []
        print(round(grass, 2), "sq m of grass")
        num_grass.append(grass)
        for x in range(5):
            t.append(rabbitage[random.randrange(0, len(rabbit))])

        print(t, "sample age of rabbits")
        t = []
        for x in range(5):
            t.append(wolfage[random.randrange(0, len(wolf))])

        print(t, "sample age of wolves")

        print(len(rabbit), "# of rabbits")
        num_rabbits.append(len(rabbit))
        print(len(wolf), "# of wolves")
        num_wolves.append(len(wolf))
        print("-------------------------------------")


import matplotlib.pyplot as plt


def graph():
    global grass, rabbit, rabbitage, wolf, wolfage, years, num_rabbits, num_wolves, num_grass

    # Data
    years = list(range(1, (years + 1)))
    grass_area = num_grass
    num_rabbits = num_rabbits
    num_wolves = num_wolves

    # Plotting
    plt.figure(figsize=(10, 6))

    # Plotting grass area
    # plt.plot(years, grass_area, marker='o', label='Grass Area')

    # Plotting number of rabbits
    plt.plot(years, num_rabbits, marker='o', label='Number of Rabbits')

    # Plotting number of wolves
    plt.plot(years, num_wolves, marker='o', label='Number of Wolves')

    # Adding labels and title
    plt.xlabel('Years')
    plt.ylabel('Quantity')
    plt.title('Population Dynamics Over 100 Years')
    plt.legend()

    # Displaying the plot
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    rabbitwolfsim()
    graph()


main()
