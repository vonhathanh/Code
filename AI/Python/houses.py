import math
import random

def get_random_neighbour(state):
    neighbour = [house[:] for house in state]  # Deep copy

    i, j = random.sample(range(7), 2)
    attr_idx = random.randint(0, 9)

    neighbour[i][attr_idx], neighbour[j][attr_idx] = neighbour[j][attr_idx], neighbour[i][attr_idx]
    return neighbour

NATION = 0
COLOR = 1
ANIMAL = 2
DRINK = 3
SMOKE = 4
FLOWER = 5
CAR = 6
FOOD = 7
TREE = 8
SPORT = 9

def cost_of_state(state):
    cost = 50
    for i, h in enumerate(state):
        cost -= sum([
            # There are two houses between the crocuses and the cats.
            h[FLOWER] == 'crocuses' and (
                (i > 2 and state[i - 3][ANIMAL] == 'cat') or (i < 4 and state[i + 3][ANIMAL] == 'cat')),
            # The person drinking soda lives directly to the right of the gray house.
            i < 6 and h[COLOR] == 'gray' and state[i + 1][DRINK] == 'soda',
            # The person smoking Chersterfields lives directly to the right of the person eating steaks.
            i < 6 and h[FOOD] == 'steak' and state[i + 1][SMOKE] == 'chesterfield',
            # The horses live directly to the left of the person drinking coffee.
            i < 6 and h[ANIMAL] == 'horse' and state[i + 1][DRINK] == 'coffee',
            # The person with birch trees has cats.
            h[TREE] == 'birch' and h[ANIMAL] == 'cat',
            # There is one house between the redwoods and the snakes.
            h[TREE] == 'redwoods' and (
                (i > 1 and state[i - 2][ANIMAL] == 'snake') or (i < 5 and state[i + 2][ANIMAL] == 'snake')),
            # The person eating potatoes lives directly next to the brown house.
            h[COLOR] == 'brown' and (
                (i > 0 and state[i - 1][FOOD] == 'potato') or (i < 6 and state[i + 1][FOOD] == 'potato')),
            # There is one house between the Tennis player and the person eating spaghetties on the right
            i < 5 and h[SPORT] == 'tennis' and state[i + 2][FOOD] == 'spagetti',
            # There is one house between the Swede and the driver of the Porsche.
            h[NATION] == 'swede' and (
                (i > 1 and state[i - 2][CAR] == 'porsche') or (i < 5 and state[i + 2][CAR] == 'porsche')),
            # The cactuses grow in front of house four.
            i == 3 and h[FLOWER] == 'cactuses',
            # There are two houses between the black and pink house on the right
            (i < 4 and h[COLOR] == 'black' and state[i + 3][COLOR] == 'pink'),
            # The dahlias grow to the right of the person drinking icetea.
            i < 6 and h[DRINK] == 'icetea' and sum([1 for x in range(i + 1, 7) if state[x][FLOWER] == 'dahilas']) > 0,
            # There is one house between the Rugby player and the person eating eggs on the right
            (i < 5 and h[SPORT] == 'rugby' and state[i + 2][FOOD] == 'egg'),
            # The person playing Badminton smokes Prince.
            h[SPORT] == 'badminton' and h[SMOKE] == 'prince',
            # There is one house between the palm trees and the person smoking Cubans on the left
            (i < 5 and h[SMOKE] == 'cuban' and state[i + 2][TREE] == 'palm'),
            # The person eating cheese lives to the left of the brown house.
            i > 0 and h[COLOR] == 'brown' and sum([1 for x in range(0, i) if state[x][FOOD] == 'cheese']) > 0,
            # The turtles live directly to the right of the person smoking Chersterfields.
            i < 6 and h[SMOKE] == 'chesterfield' and state[i + 1][ANIMAL] == 'turtle',
            # There are two houses between the black house and the house the British lives in on the right
            i < 4 and h[COLOR] == 'black' and state[i + 3][NATION] == 'british',
            # The eucalyptus trees do not grow in front of house four.
            i == 3 and h[TREE] != 'eucalyptus',
            # There are two houses between the German and the redwoods on the left
            i < 4 and h[TREE] == 'redwoods' and state[i + 3][NATION] == 'german',
            # The Renault driver lives directly next to Lacrosse player.
            h[CAR] == 'renault' and (
                (i > 0 and state[i - 1][SPORT] == 'lacrosse') or (i < 6 and state[i + 1][SPORT] == 'lacrosse')),
            # There are two houses between the VW driver and the person smoking Bluemaster on the left
            i < 4 and h[SMOKE] == 'bluemaster' and state[i + 3][CAR] == 'vw',
            # The cats live directly next to the blue house.
            h[COLOR] == 'blue' and (
                (i > 0 and state[i - 1][ANIMAL] == 'cat') or (i < 6 and state[i + 1][ANIMAL] == 'cat')),
            # There are two houses between the house of the person eating potatoes and the green house on the right
            i < 4 and h[FOOD] == 'potato' and state[i + 3][COLOR] == 'green',
            # The Rolls Royce driver lives to the right of the Volvo driver.
            i > 0 and h[CAR] == 'rollsroyce' and sum([1 for x in range(0, i) if state[x][CAR] == 'volvo']) > 0,
            # The Swiss lives directly next to the Badminton player.
            h[NATION] == 'swiss' and (
                (i > 0 and state[i - 1][SPORT] == 'badminton') or (i < 6 and state[i + 1][SPORT] == 'badminton')),
            # The Rugby player lives directly to the left of the person smoking Dunhill.
            i < 6 and h[SPORT] == 'rugby' and state[i + 1][SMOKE] == 'dunhill',
            # The person in house three drinks milk.
            i == 2 and h[DRINK] == 'milk',
            # There are two houses between the Baseball player and the person drinking wine on the right
            i < 4 and h[SPORT] == 'baseball' and state[i + 3][DRINK] == 'wine',
            # There are two houses between the tortoises and the dogs.
            h[ANIMAL] == 'tortoise' and (
                (i > 2 and state[i - 3][ANIMAL] == 'dog') or (i < 4 and state[i + 3][ANIMAL] == 'dog')),
            # There is one house between the dogs and the person drinking lemonade.
            h[ANIMAL] == 'dog' and (
                (i > 1 and state[i - 2][DRINK] == 'lemonade') or (i < 5 and state[i + 2][DRINK] == 'lemonade')),
            # There are two houses between the pink house and the house the Swede lives in on the left
            i < 4 and h[NATION] == 'swede' and state[i + 3][COLOR] == 'pink',
            # The British lives directly next to the orchids.
            h[NATION] == 'british' and (
                (i > 0 and state[i - 1][FLOWER] == 'orchids') or (i < 6 and state[i + 1][FLOWER] == 'orchids')),
            # There is one house between the house where the tulips grow and the red house.
            h[FLOWER] == 'tulips' and (
                (i > 1 and state[i - 2][COLOR] == 'red') or (i < 5 and state[i + 2][COLOR] == 'red')),
            # The person in house five does not drink wine.
            i == 4 and h[DRINK] != 'wine',
            # There is one house between the cats and the person eating chocolate on the right
            i < 5 and h[ANIMAL] == 'cat' and state[i + 2][FOOD] == 'chocolate',
            # The VW driver lives directly to the left of the Ferrari driver.
            i < 6 and h[CAR] == 'vw' and state[i + 1][CAR] == 'ferrari',
            # The Rolls Royce is not parked in front of house seven.
            i == 6 and h[CAR] != 'rollsroyce',
            # There is one house between the crocuses and the cactuses.
            h[FLOWER] == 'crocuses' and (
                (i > 1 and state[i - 2][FLOWER] == 'cactuses') or (i < 5 and state[i + 2][FLOWER] == 'cactuses')),
            # There is one house between the German and the Marlboro smoking person.
            h[NATION] == 'german' and (
                (i > 1 and state[i - 2][SMOKE] == 'marlboro') or (i < 5 and state[i + 2][SMOKE] == 'marlboro')),
            # There is one house between the willows and the person smoking Cubans on the right
            (i < 5 and h[TREE] == 'willows' and state[i + 2][SMOKE] == 'cuban'),
            # There are two houses between the Lacrosse player and the person drinking coffee on the left
            (i < 4 and h[DRINK] == 'coffee' and state[i + 3][SPORT] == 'lacrosse'),
            # The Italian lives in the blue house.
            h[NATION] == 'italian' and h[COLOR] == 'blue',
            # There are two houses between the lilies and the Tennis player on the left
            (i < 4 and h[SPORT] == 'tennis' and state[i + 3][FLOWER] == 'lilies'),
            # There is one house between the Spanish and the driver of the VW on the left.
            (i < 5 and h[CAR] == 'vw' and state[i + 2][NATION] == 'spanish'),
            # There are two houses between the turtles and the person eating eggs.
            h[ANIMAL] == 'turtle' and (
                (i > 2 and state[i - 3][FOOD] == 'egg') or (i < 4 and state[i + 3][FOOD] == 'egg')),
            # The Italian lives to the left of the Badminton player.
            i > 0 and h[SPORT] == 'badminton' and sum([1 for x in range(0, i) if state[x][NATION] == 'italian']) > 0,
            # There is one house between the lilies and the Ferrari.
            h[CAR] == 'ferrari' and (
                (i > 1 and state[i - 2][FLOWER] == 'lilies') or (i < 5 and state[i + 2][FLOWER] == 'lilies')),
            # The orchids grow to the left of the Basketball player.
            i > 0 and h[SPORT] == 'basketball' and sum([1 for x in range(0, i) if state[x][FLOWER] == 'orchids']) > 0,
            # The nut trees grow directly next to the person drinking wine.
            h[TREE] == 'nut' and (
                (i > 0 and state[i - 1][DRINK] == 'wine') or (i < 6 and state[i + 1][DRINK] == 'wine'))
        ])
    return cost

def sa(initial):
    current = initial
    current_cost = cost_of_state(current)
    temp = 1.0
    num_iterations = 0

    while current_cost > 0:
        neighbour = get_random_neighbour(current)
        neighbour_cost = cost_of_state(neighbour)
        print("neighbour cost = ", neighbour_cost)
        cost_delta = neighbour_cost - current_cost
        # print("cost delta = ", cost_delta)
        # print("e^delta = ", math.exp(-cost_delta / temp))
        if cost_delta <= 0:
            current, current_cost = neighbour, neighbour_cost

        num_iterations += 1
        if num_iterations % 500 == 0 and temp > 0.20:
            temp -= 0.05

    return current, num_iterations

def main():
    nationalities = ["british", "swede", "swiss", "german", "italian", "greek", "spanish"]
    colours = ["gray", "red", "green", "brown", "blue", "pink", "black"]
    animals = ["dog", "horse", "cat", "snake", "turtle", "tortoise", "pet"]
    drinks = ["icetea", "coffee", "milk", "wine", "soda", "lemonade", "drink"]
    cigars = ["marlboro", "prince", "cuban", "bluemaster", "dunhill", "chesterfield", "tabaco"]
    foods = ["steak", "spagetti", "egg", "potato", "cheese", "chocolate", "food"]
    sports = ["tennis", "rugby", "badminton", "lacrosse", "baseball", "basketball", "sport"]
    trees = ["tree", "eucalyptus", "redwoods", "palm", "birch", "willows", "nut"]
    flowers = ["dahilas", "lilies", "orchids", "tulips", "cactuses", "crocuses", "flower"]
    cars = ["porsche", "vw", "renault", "volvo", "rollsroyce", "ferrari", "car"]

    attributes = [nationalities, colours, animals, drinks, cigars, foods, sports, trees, flowers, cars]

    NUM_HOUSES = 7
    initial = []

    for i in range(NUM_HOUSES):
        initial.append([attr[i] for attr in attributes])

    random.seed(1000)

    solution, iterations = sa(initial)

    for house in solution:
        print(house)

    print('Number of iterations:', iterations)

if __name__ == "__main__":
    main()
