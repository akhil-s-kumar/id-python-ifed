import requests
import json

def ability(name_str):
    name = name_str
    url = 'https://pokeapi.co/api/v2/pokemon/%s'%(name)
    response = requests.get(url)
    type_data =json.loads(response.text)
    a = len(type_data['abilities'])
    lst_ability = []
    for i in range(a):
        lst_ability.append(type_data['abilities'][i]['ability']['name'])
    return lst_ability

