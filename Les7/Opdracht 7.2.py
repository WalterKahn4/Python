Woorden = []

Vraagomwoord = True
while (Vraagomwoord):
    woord = str(input('Geef een string van vier letters:'))
    if (len(woord) != 4):
        print('{} heeft {} letters'.format(woord,len(woord)))
    else:
        len(woord) == 4
        print('Inlezen van correcte string: {} is geslaagd'.format(woord))
        break