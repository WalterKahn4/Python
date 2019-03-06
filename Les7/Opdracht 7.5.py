def namen():
    namen = {}
    while(True):
        naam = input('Volgende naam: ')
        if not naam:
            print(namen)
            for naam, aantal in namen.items():
                if(aantal == 1):
                    print("Er is 1 student met de naam {}".format(naam))
                else:
                    print("Er zijn {} studenten met "
                          "de naam {}".format(aantal, naam))
        else:
            if naam in namen:
                namen[naam] += 1
            else:
                namen[naam] = 1

namen()