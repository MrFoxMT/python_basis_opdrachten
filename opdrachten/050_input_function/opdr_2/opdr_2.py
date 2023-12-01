# Opdracht 2 berekeningen
# Naam student: Milan van de Klippe
# Groep: ITX1

# Hier komt je code...

gasten = ["Milan", "Paul", "Kees", "Marie", "Hilda"]

del gasten[3]
gasten.insert(3, 'George')
print(gasten)



stad_land1 = input("Land of stad 1 ")
stad_land2 = input("Land of stad 2 ")
stad_land3 = input("Land of stad 3 ")
stad_land4 = input("Land of stad 4 ")
stad_land5 = input("Land of stad 5 ")

imputs = sorted([stad_land1, stad_land2, stad_land3, stad_land4, stad_land5])
sort = sorted(imputs, reverse=True)
print(sort)

