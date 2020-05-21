from random import randint


def draw_dice():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if draw_dice() == i:
        print('Acertou!', i)
        break
else:
    print('Errou!')
