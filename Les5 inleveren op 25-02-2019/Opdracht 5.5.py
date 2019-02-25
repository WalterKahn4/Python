zin = input('Voer een willekeurige zin in: ')

woorden = []
for woord in zin.split():
    woorden.append(len(woord))

gemiddelde = float(sum(woorden)) / len(woorden)
print(gemiddelde)