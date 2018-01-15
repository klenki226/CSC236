import random

def roll_dice():
    """give a random number from 1 to 6"""
    diceroll = random.randint(1,6)
    return diceroll

def player1(b1):
    roll = roll_dice()
    if roll == 1:
        if b1.body == 0:
            b1.body = 1
            player1(b1)
        else:
            return b1
    elif roll == 2:
        if b1.head == 0 and b1.body == 1:
            b1.head = 1
            player1(b1)
        else:
            return b1
    elif roll == 3:
        if b1.body == 1 and b1.legs != 6:
            b1.legs = (b1.legs + 2)
            player1(b1)
        else:
            return b1
    elif roll == 4:
        if b1.head == 1 and b1.eye != 2:
            b1.eye = (b1.eye + 1)
            player1(b1)
        else:
            return b1
    elif roll == 5:
        if b1.head == 1 and b1.feeler != 2:
            b1.feeler = (b1.feeler + 1)
            player1(b1)
        else:
            return b1
    elif roll == 6:
        if b1.body == 1 and b1.tail == 0:
            b1.tail = 1
            player1(b1)
        else:
            return b1
    return b1

def player2(b2):
    roll = roll_dice()
    if roll == 1:
        if b2.body == 0:
            b2.body = 1
            player2(b2)
        else:
            return b2
    elif roll == 2:
        if b2.head == 0 and b2.body == 1:
            b2.head = 1
            player2(b2)
        else:
            return b2
    elif roll == 3:
        if b2.body == 1 and b2.legs != 6:
            b2.legs = (b2.legs + 2)
            player2(b2)
        else:
            return b2
    elif roll == 4:
        if b2.head == 1 and b2.eye != 2:
            b2.eye = (b2.eye + 1)
            player2(b2)
        else:
            return b2
    elif roll == 5:
        if b2.head == 1 and b2.feeler != 2:
            b2.feeler = (b2.feeler + 1)
            player2(b2)
        else:
            return b2
    elif roll == 6:
        if b2.body == 1 and b2.tail == 0:
            b2.tail = 1
            player2(b2)
        else:
            return b2
    return b2

def main():
    beetle1 = 'beetle.Beetle'
    beetle2 = 'beetle.Beetle'
    while (beetle1.head != 1 and beetle1.body != 1 and beetle1.legs != 6 and beetle1.eye != 2 and beetle1.feeler != 2 and beetle1.tail != 1) or (beetle2.head != 1 and beetle2.body != 1 and beetle2.legs != 6 and beetle2.eye != 2 and beetle2.feeler != 2 and beetle2.tail != 1):
        player1(beetle1)
        player2(beetle2)

    if beetle1.head == 1 and beetle1.body == 1 and beetle1.legs == 6 and beetle1.eye == 2 and beetle1.feeler == 2 and beetle1.tail == 1:
        print('player 1 wins')
    elif beetle2.head == 1 and beetle2.body == 1 and beetle2.legs == 6 and beetle2.eye == 2 and beetle2.feeler == 2 and beetle2.tail == 1:
        print('player 2 wins')

main()

