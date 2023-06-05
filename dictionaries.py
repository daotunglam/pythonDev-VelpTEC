
import random


dic = {"Namen": ["Thor"], "Berufe": ["Donnergott"], "Heimatorte": ["Asgard"]}


def func(dictionary, namenliste, berufsliste, ortsliste):
    dictionary['Namen'].extend(namenliste)
    dictionary['Berufe'].extend(berufsliste)
    dictionary['Heimatorte'].extend(ortsliste)
    return dictionary


namenliste = ["Loki", "Odin"]
berufsliste = ["Gott", "König"]
ortsliste = ["Jotunheim", "Walhalla"]

func(dic, namenliste, berufsliste, ortsliste)
# print(dic)


names = ["Max", "Sophie", "Liam", "Emma", "Noah"]
places = ["Berlin", "Paris", "London", "New York", "Tokyo"]

def random_personenprofil(namenliste, ortsliste):
    personenprofil = {'Name': '',
                      'Alter': '',
                      'Ort': ''}
    personenprofil["Name"] = namenliste[random.randint(0,len(names)-1)]
    personenprofil["Alter"] = random.randint(18,85)
    personenprofil["Ort"] = ortsliste[random.randint(0,len(places)-1)]
    return personenprofil

def create_database(number_of_data):
    return [random_personenprofil(names, places) for _ in range(number_of_data)]

print(create_database(10))
