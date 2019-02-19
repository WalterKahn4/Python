def convert(graden_celsius):
    graden_fahrenheit = graden_celsius * 1.8 + 32
    print(str(graden_fahrenheit) + 'ᴼF')

def tabel(c):
    for i in range(-30, 50,10):
        c = c+10
        f = c*1.8+32
        print('{:4} {:4}'.format(float(f),float(c)))