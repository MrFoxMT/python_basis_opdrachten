# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....

print("De rivier de", rivieren[0].capitalize(), "stroomt onder andere door", rivier_info["rijn"][1].capitalize())

print("De rivier de", rivieren[1].capitalize(), "stroomt onder andere door", rivier_info["maas"][0].capitalize())

print("De rivier de", rivieren[2].capitalize(), "stroomt onder andere door", rivier_info["nijl"][1].capitalize())





