""" 
Problem 84

In the game, Monopoly, the standard board is set up in the following way: (https://projecteuler.net/problem=84)

A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they 
advance in a clockwise direction. Without any further rules we would expect to visit each square with equal 
probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, 
if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they 
proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card 
from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. 
There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order 
a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL

Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing 
at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability 
of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another 
square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no 
distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double 
to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to 
produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are 
JAIL (6.24%) = Square 10, 
E3 (3.18%) = Square 24, 
and GO (3.09%) = Square 00. 
So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

"""

import time
import math
import random


def calculate() -> int:

    # current location
    location = 0

    # double counter
    double_count = 0

    # init game
    board = init_board()
    chance = init_chance()
    community_chest = init_community_chest()

    # test dice
    for y in range(1000000):

        # roll check
        dice = roll()

        # double check
        if is_double(dice):
            double_count += 1
        else:
            double_count = 0

        # if 3 doubles, go to jail
        if double_count == 3:
            location = 10
            board[location][1] += 1
            double_count = 0
            continue

        location = move(location, dice)

        # lands on go to jail
        if location == 30:
            location = 10
            board[location][1] += 1
            continue

        # lands on chance
        if is_chance(location):
            # print(f"{dice} !!! You landed on chance")
            if len(chance) == 0:
                chance = init_chance()
            card = chance.pop()
            move_modifier = draw_chance(card, location)
            if move_modifier != -1:
                location = move_modifier
            board[location][1] += 1
            continue

        # lands on community chest
        if is_community_chest(location):
            # print(f"{dice} !!! You landed on community chest")
            if len(community_chest) == 0:
                community_chest = init_community_chest()
            card = community_chest.pop()
            move_modifier = draw_community_chest(card)
            if move_modifier != -1:
                location = move_modifier
            board[location][1] += 1
            continue

        # all other scenarios
        board[location][1] += 1

    top3 = get_top_3(board)
    output = str(top3[0][0]) + str(top3[1][0]) + str(top3[2][0])
    return int(output)


def roll() -> list:
    dice = []
    # print("\nRolling...")
    dice.append(random.randint(1, 4))
    dice.append(random.randint(1, 4))
    # print(f"--> {dice}")
    return dice


def is_double(dice) -> bool:
    output = dice[0] == dice[1]
    # if output:
    # 	print(f"{dice} is a double -> player would roll again")
    # else:
    # 	print(f"{dice} is not double -> end of turn")
    return output


def roll_total(dice) -> int:
    output = sum(dice)
    # print(f"{dice} results in a movement of {output}")
    return output


def init_board() -> list:
    output = []
    for i in range(40):
        tile = [i, 0]
        output.append(tile)
    return output


def move(current_location, dice) -> int:
    output = current_location + roll_total(dice)
    if output > 39:
        output -= 40
    return output


def is_chance(location) -> bool:
    chance_locations = [7, 22, 36]
    return location in chance_locations


def is_community_chest(location) -> bool:
    chance_locations = [2, 17, 33]
    return location in chance_locations


def init_chance() -> list:
    output = [
        "Advance to GO",
        "Go to JAIL",
        "Go to C1",
        "Go to E3",
        "Go to H2",
        "Go to R1",
        "Go to next Railroad",
        "Go to next Railroad",
        "Go to next Utility",
        "Go back 3 squares.",
    ]
    for i in range(6):
        output.append("Nothing")
    random.shuffle(output)
    return output


def init_community_chest() -> list:
    output = ["Advance to GO", "Go to JAIL"]
    for i in range(14):
        output.append("Nothing")
    random.shuffle(output)
    return output


def draw_chance(card, current_location) -> int:
    # print(f"Chance drawn was {card}")
    if card == "Advance to GO":
        return 0
    elif card == "Go to JAIL":
        return 10
    elif card == "Go to C1":
        return 11
    elif card == "Go to E3":
        return 24
    elif card == "Go to H2":
        return 39
    elif card == "Go to R1":
        return 5
    elif card == "Go to next Railroad":
        output = current_location
        while True:
            if output % 5 == 0 and output % 2 == 1:
                return output
            output += 1
            if output == 40:
                output = 0
    elif card == "Go to next Utility":
        if current_location > 12 and current_location <= 28:
            return 28
        else:
            return 12
    elif card == "Go back 3 squares":
        output = current_location - 3
        if output < 0:
            output += 40
        return output
    else:
        return -1


def draw_community_chest(card) -> int:
    # print(f"Community Chest drawn was {card}")
    if card == "Advance to GO":
        return 0
    elif card == "Go to JAIL":
        return 10
    else:
        return -1


def get_top_3(board) -> list:
    top_3 = [[0, 0], [0, 0], [0, 0]]
    for square in board:
        if square[1] > top_3[2][1]:
            top_3[2] = square
        if square[1] > top_3[1][1]:
            top_3[2] = top_3[1]
            top_3[1] = square
        if square[1] > top_3[0][1]:
            top_3[1] = top_3[0]
            top_3[0] = square
    return top_3


if __name__ == "__main__":
    start_time = time.time()
    print(f"The answer to Problem 84 is {calculate()}")
    end_time = time.time()
    print(f"This solution took {end_time - start_time} seconds to run")
