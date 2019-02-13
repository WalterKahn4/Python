age = int(input('What is your age?'))

if age >= 62:
    print('You can get your pension benefits!')
print(30 * '_')

players = ('Musial','Aaron','Williams','Gehrig','Ruth')

name = input('Name a baseball player?')

if name in players:
    print('One of the top 5 baseball players, ever!')
print(30 * "_")

hits = int(input('How many hits?'))
Shield = int(input('How much shield?'))

if hits > 10 and Shield == 0:
    print('You are dead!')
print(30 * "_")

Dir = str(input('What direction do you want to go?'))
Wind = ('North','South','East','West')

if Dir == Wind:
    print('I can escape!')

