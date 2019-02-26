studentencijfers = [[95,92,86],[66,75,54],[34,0,0]]
def gemiddelde_per_student(studentencijfers):
    antw = []
    for cijfers in studentencijfers:
        antw.append(round(sum(cijfers)/len(cijfers)))
    return antw
def gemiddelde_van_alle_studenten(studentencijfers):
    gemiddelde_per_student = []
    for cijfers in studentencijfers:
        gemiddelde_per_student.append(round(sum(cijfers) / len(cijfers)))
    antw = round(sum(gemiddelde_per_student) / len(gemiddelde_per_student))
    return antw
print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))