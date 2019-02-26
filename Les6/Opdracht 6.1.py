def seizoen(maand):
    if maand in list[0]:
        print('it is winter!')
    elif maand in list[1]:
        print('it is spring!')
    elif maand in list[2]:
        print('it is summer!')
    elif maand in list[3]:
        print('it is autumn!')

list = [['Januari','Februari','Maart'],['April','Mei','Juni'],['Juli','Augustus','September'],['Oktober','November','December']]

seizoen('Januari')
seizoen('April')
seizoen('Augustus')
seizoen('November')