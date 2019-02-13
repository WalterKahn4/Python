Year = int(input('What year is it?'))

if Year / 4 == 0:
    print('Could be a leap year!')
else:
    print('Definitely not a leap year!')
print(30 * "_")

Lotty = str(input('What was your number?'))
Winningnum ='123456789'

if Lotty == Winningnum:
    print('You won!')
else:
    print('Better luck next time!')