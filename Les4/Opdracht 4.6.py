def wijzig(letterlijst):
    letterlijst[0]='d'
    letterlijst[1]='e'
    letterlijst[2]='f'

lijst = ['a','b','c']
print(lijst)
wijzig(lijst)
print(lijst)

#Omdat het allemaal losse strings zijn

#werkt niet met een string statement want een str is immutable

#in een lijst zitten meerdere strings deze
#stings zijn immutable maar de lijst zelf is wel mutable