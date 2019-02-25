i = 7
while i <= 37:
    i += 7

def hello():
    '''a greeting service; it repeatedly requests the name of the user and then greets the user'''
    while True:
        name = input('What is your name?')
        print('hello {}'.format(name))

def cities2():
    lst = []

    while True:
        city = input('Enter city: ')

        if city == '':
            break
        lst.append(city)

return lst

def before0():
    for row in table:
        for num in row:
            if num == 0:
                break
            print(num, end=' ')
        print()

def sum():
    total = 0
    while True:
        nextInt = input('next int: ')
        if nextInt == 'quit':
            break
        total += int(nextInt)
    print(total)

employee = []
employee.append('Yin')
employee.append('Waad')

employee[0]
employee[1]

emplyee = {}
