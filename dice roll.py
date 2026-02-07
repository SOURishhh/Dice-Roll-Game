import random

while True:
    choice = input('Ready to roll the dice ? (y/n) : ').lower()
    if choice == 'y' :
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'you got {die1} and {die2}')
    elif choice == 'n' :
        print('ok , maybe next time ?!')
        break
    else :
        print('nah not a valid choice ! , try again !')
