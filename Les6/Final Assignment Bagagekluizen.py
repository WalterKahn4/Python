open('kluizen.py', 'r')

print('1: Ik wil weten hoeveel kluizen nog vrij zijn \n'
         '2: Ik wil een nieuwe kluis \n'
         '3: IK wil even iets uit mijn kluis halen \n'
         '4: Ik geef mijn kluis terug')

keuze=int(input('Wat wil u doen?'))

if keuze == 1:
    vrijekluizen = toon_aantal_kluizen_vrij()
    print(aantalKluizen)
elif keuze == 2:
    nieuw = nieuwe_kluis()
    print(nieuw)
elif keuze == 3:
    open = kluis_openen()
    print(open)
elif keuze == 4:
    terug = kluis_teruggeven()
    print(terug)

def toon_aantal_kluizen_vrij():
    infile = open('kluizen.py','r')
    lstRegels = infile.readlines()
    aantalKluizen = len(lstRegels)
    return aantalKluizen

def nieuwe_kluis():
    kluisnummers = [1,2,3,4,5,6,7,8,9,10,11,12]
    infile = open('kluizen.py')
    regels = infile.readlines()
    for regel in regels:
        onderdelen = regel.split(';')
        kluisnr = int(onderdelen[0])
        kluisnummers.remove(kluisnr)
    infile.close()
    infile = open('kluizen.py', 'a')
    infile.write(#)
    infile.close()

def kluis_openen():
    infile = open('kluizen.py', 'r')
