# Opdracht 2 berekeningen
# Naam student: Milan van de Klippe
# Groep: ITX1

# Hier komt je code...

print("Hello, this is a calculator that can convert celsius to fahrenheit, and the other way around.")

def get_input(eenheid):
    while True:
        if eenheid == "C":
            fah = input("Type the amount of fahrenheit that u want to convert: ")
            if fah.isdigit():
                return int(fah)
            else:
                print("Please only use digits!")
        elif eenheid == "F":
            cel = input("Type the amount of celcius that u want to convert: ")
            if cel.isdigit():
                return int(cel)
            else:
                print("Please only use digits!")

def get_eenheid():
    while True:
        eenheid = input("Type C to convert to celcius and F to convert to fahrenheit: ")
        if eenheid.upper() in ["C", "F"]:
            return eenheid.upper()
        else:
            print("Please use C and F only!")

eenheid = get_eenheid()
temperature = get_input(eenheid)
def calculate(eenheid, temperature):
    if eenheid == "C":
        fahrenheit = temperature * (9.0 / 5.0) + 32
        print(f"{temperature} degrees Celsius equals to {fahrenheit:.1f} degrees Fahrenheit")
    elif eenheid == "F":
        celsius = (temperature - 32) * 5.0 / 9.0
        print(f"{temperature} degrees Fahrenheit equals to {celsius:.1f} degrees Celsius")


calculate(eenheid, temperature)
