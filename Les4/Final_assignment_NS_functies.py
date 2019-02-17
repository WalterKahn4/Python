0toename = 15

def standaardprijs(afstandKM):
    kost = 0.8 * afstandKM
    if int(afstandKM) > 50:
        kost2 = float(kost) + 15 #15 euro is de toename als de afstand groter is dan 50 gedefinieerd in lijn 1
        print(kost2)
    else:
        print(kost)

def ritprijs(leeftijd,weekendrit,afstandKM):
    x = standaardprijs
    print(x)
    dag = input('Welke dag is?')
    dagen = ['maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag']
    if dag == ('Zaterdag','Zondag'):
        print('het is ' + dag + '!')
    else:
        print('het is ' + dag + '!')
    if dag == ('maandag','dinsdag','woensdag','donderdag','vrijdag'):
        and leeftijd <= 12 or leeftijd >= 65
        leeftijdkorting = float(x) * 0.7
        print('Uw nieuwe rit prijs is ' + str(leeftijdkorting) + "!")
    else:
        print('Uw behoud de standaardrit prijs!')

