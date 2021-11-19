import requests

def card_data(name):
    name = name.replace(" ", "+")
    name = name.replace(",", "")
    endpoint = "https://api.scryfall.com/cards/named?fuzzy="
    r = requests.get(endpoint + name)

    card_data_full = r.json()
    card_data_needed = {
        "image": card_data_full['image_uris']['large'],
        "mana_cost": card_data_full['mana_cost'],
        "type_line": card_data_full['type_line'],
        "oracle_text": card_data_full['oracle_text']
        }

    return card_data_needed["image"]
