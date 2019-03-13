def monopolyworp():
    import random
    worp1 = random.randrange(1,7)
    worp2 = random.randrange(1,7)
    totaal1 = worp1+worp2
    print(worp1, '+', worp2, '=', totaal1)
    if worp1 == worp2:
        print('dubbel')
        worp3 = random.randrange(1,7)
        worp4 = random.randrange(1,7)
        totaal2 =worp3+worp4
        print(worp3, '+' ,worp4, '=',totaal2)
        if worp3 == worp4:
            print('dubbel')
            worp5 = random.randrange(1, 7)
            worp6 = random.randrange(1, 7)
            totaal3 = worp5 + worp6
            print(worp5, '+', worp6, '=',totaal3)
            if worp5 == worp6:
                print(str(worp5) + '+' +str(worp6) + '= dubbel direct naar de gevangenis!')

monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()
monopolyworp()