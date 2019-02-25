file = open('kaartnummers.py', 'r')
content = file.read()
file.close()
for line in content.splitlines():
    kaartnummer, klant = line.split(',')
    print('{} heeft kaartnummer: {}'.format(klant, kaartnummer))