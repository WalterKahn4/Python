def inlezen_beginstation(stations):
    while(True):
        station = input('Wat is je beginstation? : ')
        if station in stations:
            return station
    return

def inlezen_eindstation(stations, beginstation):
    while(True):
        station = input('Wat is je eindstation? : ')
        if station in stations:
            if(stations.index(station) > stations.index(beginstation)):
                return station
        print('Deze trein komt niet in {}'.format(station))
    return

def omroepen_reis(stations, beginstation, eindstation):
    beginstationIndex = stations.index(beginstation)
    print('\nHet beginstation {} is het {}e station in het '
          'traject.'.format(beginstation, beginstationIndex + 1))
    eindstationIndex = stations.index(eindstation)
    print('Het eindstation {} is het {}e station in het '
          'traject.'.format(eindstation, eindstationIndex + 1))
    verschil = abs(beginstationIndex - eindstationIndex)
    print('De afstand bedraagt {} station(s).'.format(verschil))
    prijs = verschil * 5
    print('De prijs van het kaartje is {} euro\n'.format(prijs))
    print('Jij stapt in de trein in: {}'.format(beginstation))
    for index, station in enumerate(stations):
        if index > beginstationIndex and index < eindstationIndex:
            print(' - {}'.format(station))
    print('Jij stapt uit in {}'.format(eindstation))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam',
            'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel',
            'Utrecht Centraal', '\'-Hertogenbosch', 'Eindhoven', 'Weert',
            'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)