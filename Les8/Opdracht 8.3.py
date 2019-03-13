def code(invoerstring):
    asciiCode = ''
    for karakter in invoerstring:
        asciiCode += chr(ord(karakter) + 3)
    return asciiCode

gebruiker = input('Gebruikersnaam: ')

beginstation = input('Bij welk station begint de reis: ')

eindstation = input('Bij welk station eindigt de reis: ')

asciiCode = code(gebruiker+beginstation+eindstation)
print(asciiCode)