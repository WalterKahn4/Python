from random import randint #importeert de mogelijkheid tot het creeren van random getallen

file = open('kluizen.txt', 'a+')
file.seek(0)
file.close()

#functie 1 het krijgen van een nieuwe kluis
def nieuwe_kluis():
    file = open('kluizen.txt', 'r+')
    kluizen = []
    for kluis in file.readlines():
        kluizen.append(int(kluis.split(',')[0]))
    if(len(kluizen) < 12):
        for i in range(0, 12):
            if i + 1 not in kluizen:
                code = str(randint(1000, 9999))
                file.write(str(i + 1) + ',' + code + '\n')
                print('Kluisnummer {} met code {} '
                      'is toegewezen.\n'.format(str(i + 1), code))
                file.seek(0)
                break
    file.close()

#functie 2 het openen van een kluis
def kluis_openen():
    file = open('kluizen.txt', 'r')
    codeInput = int(input('Voer 4-cijferige code in: '))
    kluizen = []
    for kluis in file.readlines():
        nummer, code = kluis.split(',')
        kluizen.append([int(nummer), int(code.rstrip())])
    for kluis in kluizen:
        if codeInput == kluis[1]:
            print('Kluis met nummer {} is geopend.\n'.format(kluis[0]))
            return
    print('Foutmelding! Er bestaat geen kluis met deze code.\n')
    file.close()

#functie 3 opgeven van de kluis
def kluis_opgeven():
    file = open('kluizen.txt', "r+")
    codeInput = int(input('Voer 4-cijferige code in: '))
    kluizen = []
    for kluis in file.readlines():
        nummer, code = kluis.split(',')
        kluizen.append([int(nummer), int(code.rstrip())])
    nieuweRegels = []
    for kluis in kluizen:
        if codeInput != kluis[1]:
            nieuweRegels.append('{},{}\n'.format(kluis[0], kluis[1]))
    file.seek(0)
    file.truncate()
    file.writelines(nieuweRegels)
    file.close()

#functie 4 het aantal vrije kluizen
def aantal_kluizen_vrij():
    file = open('kluizen.txt', 'r')
    file.seek(0)
    aantalVrij = 12 - len(file.readlines())
    print('Er zijn {} kluisjes vrij.\n'.format(aantalVrij))
    file.close()

isBezig = True

while(isBezig):
    print('1: Ik wil een nieuwe kluis\n'
          '2: Ik wil mijn kluis openen\n'
          '3: Ik geef mijn kluis terug\n'
          '4: Ik wil weten hoeveel kluizen nog vrij zijn''\n'
          '5: Ik wil stoppen\n''')

    menukeuze = int(input('Kies een menu optie: '))

    if menukeuze == 1:
        nieuwe_kluis()
    elif menukeuze == 2:
        kluis_openen()
    elif menukeuze == 3:
        kluis_opgeven()
    elif menukeuze == 4:
        aantal_kluizen_vrij()
    else:
        isBezig = False