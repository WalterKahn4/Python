toename = 15

def standaardprijs(afstandKM):
    kost = 0.8 * afstandKM
    if afstandKM == 0:
        print('0')
    if int(afstandKM) > 50:
        kost2 = float(kost) + 15 #15 euro is de toename als de afstand groter is dan 50 gedefinieerd in lijn 1
        print(kost2)
    else:
        print(str(kost))

def ritprijs(leeftijd,weekendrit,afstandKM):
    if afstandKM == 0:
        print('Uw kosten zijn 0!')
    else:
        kost = 0.8 * afstandKM
        int(afstandKM) > 50
        kost = float(kost) + 15
        or:
            kost = 0.8 * afstandKM
    dag = weekendrit
    dagen = ['maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag']
    if dag == ('Zaterdag','Zondag') and leeftijd <=65 or leeftijd >= 65:
        Weekendprijs = x * 0.65
        print('het is ' + dag + '! en uw ritprijs is' + weekendrit)
    else:
        if dag == ('maandag','dinsdag','woensdag','donderdag','vrijdag') and leeftijd <= 12 or leeftijd >= 65:
            leeftijdkorting = float(x) * 0.7
            print('Uw nieuwe rit prijs is ' + str(leeftijdkorting) + "!")
        else:
            if dag == ('maandag','dinsdag','woensdag','donderdag','vrijdag') and leeftijd > 13 or leeftijd < 65:
                leeftijdsgroep = int(x) * 0.6
                print('uw ritprijs is' + str(leeftijdsgroep))
            else:
                print('uw krijgt geen korting uw ritprijs blijft' + str(x) + '!')
