def ticker(filename):
    file = open(filename, 'r')
    symbolen = {}
    for line in file.readlines():
        bedrijf, symbool = line.rstrip().split(':')
        symbolen[bedrijf] = symbool
    file.close()
    return symbolen

symbolen = ticker('tickersymbol.py')

bedrijf = input('Enter Company name: ')
print('Ticker symbol: {}\n'.format(symbolen[bedrijf]))

ticker = input('Enter Ticker symbol: ')
bedrijf = list(symbolen.keys())[list(symbolen.values()).index(ticker)]
print('Company name: {}'.format(bedrijf))
