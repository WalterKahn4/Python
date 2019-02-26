invoer = '5-9-7-1-7-8-3-2-4-8-7-9'

getallen = list(map(int, invoer.split('-')))
getallen.sort()

grootste = max(getallen)

kleinste = min(getallen)

aantal = len(getallen)

som = sum(getallen)

gemiddelde = sum(getallen)/len(getallen)

print('''Gesoorteerde lijst van int: {}
 Grootste getal: {}
 en Kleinste getal: {} Aantal getallen: {}
 en Som van de getallen: {} Gemidddelde: {}'''.format(getallen,grootste,kleinste,aantal,som,gemiddelde))

