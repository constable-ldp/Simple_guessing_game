import random

x = -1
while True:
    if 0 < x < 11:
        break
    else:
        print('Please input an integer between 0 and 10:')
        try:
            x = int(input())
        except:
            while False:
                print('Please input an integer between 0 and 10:')
                x = int(input())
y = random.randint(0,10)

if x == y:
    print('The computer guessed your number')
else:
    print(f'The computer guessed {y} but your number was {x}')


