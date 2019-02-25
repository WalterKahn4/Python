from datetime import datetime
file = open('hardlopers.py', 'a+')
hardloper = input('Naam hardloper: ')
tijd = datetime.strftime(datetime.now(), '%a%e %b %G, %H:%M:%S')
file.write(tijd + ', ' + hardloper + '\n')
file.close()