import random

print('printing random number')
createNumber = print(random.randint(1,9))
guessNumber = input('Guess what number im thinking of between 1 and 9? ')

if (guessNumber == createNumber ):
    print('Good Job')
else:
    print('whoops thats wrong')

    
