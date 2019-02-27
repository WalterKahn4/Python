open('kluizen.py', 'r')

print('1: Ik wil weten hoeveel kluizen nog vrij zijn \n'
         '2: Ik wil een nieuwe kluis \n'
         '3: IK wil even iets uit mijn kluis halen \n'
         '4: Ik geef mijn kluis terug')

keuze=int(input('Wat wil u doen?'))

if keuze == 1:
    vrijekluizen = toon_aantal_kluizen_vrij()
    print(vrijekluizen)
elif keuze == 2:
    nieuw = nieuwe_kluis()
    print(nieuw)
elif keuze == 3:

elif keuze == 4:

def toon_aantal_kluizen_vrij():
    infile = open('kluizen.py','r')
    lstRegels = infile.readlines()
    aantalKluizen = len(lstRegels)
    return aantalKluizen

def nieuw_kluis():
