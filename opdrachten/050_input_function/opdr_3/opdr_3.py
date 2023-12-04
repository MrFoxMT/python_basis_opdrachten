# Opdracht 3 input functie
# Naam student: Milan van de Klippe
# Groep: ITX1

# Hier komt je code...

def user_input():
    while True:
        print("Typ 5 steden, of landen naar keuze.")
        stad_land1 = input("Land of stad 1 ")
        stad_land2 = input("Land of stad 2 ")
        stad_land3 = input("Land of stad 3 ")
        stad_land4 = input("Land of stad 4 ")
        stad_land5 = input("Land of stad 5 ")
        inputs = sorted([stad_land1, stad_land2, stad_land3, stad_land4, stad_land5], reverse=True)

        print(f"Sorted inputs: {inputs}")

        confirm = input("Dit zijn uw ingevoerde steden of landen, wilt u doorgaan? Typ dan Y of N ")

        if confirm == "Y":
            print("We gaan door.")
            break
        elif confirm == "N":
            print("We gaan terug.")
            continue
        else:
            print("Please only use Y or N")



user_input()


print("Bedankt")
