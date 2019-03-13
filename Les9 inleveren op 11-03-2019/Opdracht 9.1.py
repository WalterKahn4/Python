try:
    aantalReizigers = int(input('Hoeveel personen gaan er mee op reis? : '))
    if aantalReizigers == 0:
        raise Exception('Delen door nul kan niet!')
    elif aantalReizigers < 0:
        raise Exception('Negatieve getallen zijn niet toegestaan!')
    elif isinstance(aantalReizigers, str):
        raise Exception('Gebruik cijfers voor het invoeren van het aantal!')
except Exception:
    print()
except ValueError:
    print('Onjuiste invoer!')

print('De kosten voor 1 persoon '
      'bedraagt: {0:.2f}'.format(4356 / aantalReizigers))