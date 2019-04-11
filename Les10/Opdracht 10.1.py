import xmltodict

with open('artikelen.xml') as file:
    document = xmltodict.parse(file.read())
    for artikel in document['artikelen']['artikel']:
        print(artikel['naam'])