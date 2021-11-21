import requests

def card_data(name):
    name = name.replace(" ", "+")
    name = name.replace(",", "")
    endpoint = "https://api.scryfall.com/cards/named?fuzzy="
    r = requests.get(endpoint + name)

    card_data_full = r.json()
    card_data_needed = ""

    if "image_uris" in card_data_full.keys():
        card_data_needed = card_data_full['image_uris']['large']

    else:
        for element in card_data_full["card_faces"]:
            card_data_needed  = card_data_needed + element['image_uris']['large'] + " "

    return card_data_needed
