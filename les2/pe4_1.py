print('Hallo student')

cijferICOR = input('Welk cijfer heb je gehaald voor de cursu ICOR?')
cijferPROG = input('Welk cijfer heb je gehaald voor de cursus PROG?')
cijferCSN = input('Welk cijfer heb je gehaald voor de cursus CSN')

gemcijfer = (float(cijferICOR)+float(cijferPROG)+float(cijferCSN))/3

print('je gemiddelde cijfer is een ' + str(gemcijfer) + ' uit 10!')

geldbeloning = 30.0

beloningICOR = (int(cijferICOR)*geldbeloning)
beloningPROG = (int(cijferPROG)*geldbeloning)
beloningCSN = (int(cijferCSN)*geldbeloning)

print('je beloning voor de cursus ICOR is ' + str(beloningICOR))
print('je beloning voor de cursus PROG is ' + str(beloningPROG))
print('je beloning voor de cursus CSN is ' + str(beloningCSN))

totalebeloning = (int(beloningICOR)+int(beloningPROG)+int(beloningCSN))

print('De totale beloning voor blok 1 bedraagt ' + str(totalebeloning) + ' euro!')

print('Mijn cijfer (gemiddeld een ' + str(gemcijfer) + ') leveren een beloning van € ' + str(totalebeloning) + ' op!' )