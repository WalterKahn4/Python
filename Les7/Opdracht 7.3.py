studenten = {
    'Donny van Walsem':  [5, 6, 9],
    'Lesley Oudshoorn':  [7, 8, 9],
    'Yannick Thomassen': [9, 8, 10]
}

for student, cijfers in studenten.items():
    cijfersBovenNegen = []
    for cijfer in cijfers:
        if cijfer >= 9:
            cijfersBovenNegen.append(cijfer)
    print('{0:17} {1}'.format(student,cijfersBovenNegen))
