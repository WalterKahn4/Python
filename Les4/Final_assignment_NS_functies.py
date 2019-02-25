def standaardprijs(afstandKM):
    prijs = 0
    if int(afstandKM) < 0:
        return prijs

    if int(afstandKM) > 50:
        prijs = 15 + 0.6 * int(afstandKM)
    else:
        prijs = 0.8 * int(afstandKM)
    return prijs


def ritprijs(leeftijd, weekendrit, afstand):
    standaardPrijs = standaardprijs(afstand)
    korting = 1
    if int(leeftijd) < 12 or int(leeftijd) >= 65:
        if weekendrit:
            korting -= 0.3
        else:
            korting -= 0.35
    else:
        if weekendrit:
            korting -= 0.4
    return standaardPrijs * korting


leeftijd = input("blabllalba leeftijd?: ")
weekendritInput = input("blalbalba weekendrit: ")
weekendrit = True
if weekendritInput != 1:
    weekendrit = False
afstandKM = input("blalblab afstand: ")

print(ritprijs(leeftijd, weekendrit, afstandKM))

# print(ritprijs(11, 1, 300))
# print(ritprijs(11, 0, 300))
