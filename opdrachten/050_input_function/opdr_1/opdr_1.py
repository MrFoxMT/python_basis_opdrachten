# Opdracht 1 input function
# Naam student: Milan van de Klippe
# Groep: ITX1

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.
import math

print("Type de lengte van 2 zijden van een driehoek.")

zijde1 = float(input("De lengte van rechte zijde 1: "))
zijde2 = float(input("De lengte van rechte zijde 2: "))

allebij_zijden = zijde1 ** 2 + zijde2 ** 2

wortel_af = math.sqrt(allebij_zijden)

wortel_af_round = round(wortel_af, 2)
print("De lengte van de schuine zijde is " + str(wortel_af_round) + " als zijde 1 " + str(zijde1) + " is, en als zijde 2 " + str(zijde2) + " is.")

