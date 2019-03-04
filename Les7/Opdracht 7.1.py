getallen = []

vraagOmGetal = True
while(vraagOmGetal):
    getal = int(input('Geef een getal op: '))
    if(getal != 0):
        getallen.append(getal)
    else:
        vraagOmGetal = False
        print('Er zijn {} getallen ingevoerd, '
              'de som is: {}'.format(len(getallen), sum(getallen)))