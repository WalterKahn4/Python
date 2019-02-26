eval(input("Geef lijst met minimaal 10 strings: "))

list = ['boter','kaas','bier','pizza','thee','drop','koek','cola','boterham','stamppot']

newlist = []
for string in list:
    if len(string) == 4:
        newlist.append(string)

print(newlist)