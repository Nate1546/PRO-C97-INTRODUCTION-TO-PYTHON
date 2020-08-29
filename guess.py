import random
print('Hello! What is your name?')
myName = input()
print('guess a number')
number = input()

n = random.randint(0,22)


if n == number:
    print('Yay you won.') 
else:
    print('nope your number is'),
    print(n) 