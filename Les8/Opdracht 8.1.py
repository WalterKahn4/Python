bruin = {'Boxtel','Best','Beukenlaan','Eindhoven','Helmond "t hout','Helmond',
         'Helmond Brouwhuis','Deurne'}
groen = {'Boxtel','Best','Beukenlaan','Eindhoven','Geldrop','Heeze','Weert'}

def overeenkomst():
    over = bruin.intersection(groen)
    print(over)

def verschil():
    vers = bruin.difference(groen)
    print(vers)

def allestations():
    over = bruin.intersection(groen)
    vers = bruin.difference(groen)
    vers2 = groen.difference(bruin)
    alle1 = vers2.union(over)
    alle2 = alle1.union(vers)
    print(alle2)

overeenkomst()
verschil()
allestations()


