file = open('kaartnummers.py', 'r')
content = file.read()
file.close()
aantalRegels = len(content.splitlines())
i = 0
kaartnummers = []
for index, line in enumerate(content.splitlines()):
    kaartnummer, klant = line.split(',')
    kaartnummers.append((kaartnummer, index + 1))
grootsteKaartnummer = max(kaartnummers)[0]
opRegel = max(kaartnummers)[1]
print('Deze file telt {} regels.\n Het grootste kaartnummer is: {} en dat staat '
      'op regel {}'.format(aantalRegels, grootsteKaartnummer, opRegel))
