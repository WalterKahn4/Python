teRadenWoord = "Guide van Rossum heeft programmeertaal Python bedacht"

weerTeGevenWoord = ""

for letter in teRadenWoord:
    if letter in ['a', 'e', 'o', 'u']:
        weerTeGevenWoord += letter
    else:
        weerTeGevenWoord += '_'

print(weerTeGevenWoord)