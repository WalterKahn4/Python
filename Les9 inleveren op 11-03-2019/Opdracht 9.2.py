from datetime import datetime
import csv

bestand = 'inloggers.csv'

with open('inloggers.csv', 'w') as file:
    while(True):
        naam = input("Wat is je achternaam? ")
        if(naam == 'einde'):
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        tijdstip = datetime.strftime(datetime.now(), '%a %d %b %G at %H:%M')
        text = [tijdstip, voorl, naam, gbdatum, email]
        file.write(';'.join(text))
        file.write('\n')