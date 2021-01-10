import PySimpleGUI as sg
import requests
import json

layout = [[sg.Text("Pokemon Name")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT1-')],
          [sg.Text(size=(40,1), key='-OUTPUT2-')],
          [sg.Text(size=(80,1), key='-OUTPUT3-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

window = sg.Window('Pokedex', layout)

# To get Type Name
name = 'psyduck'
url = 'https://pokeapi.co/api/v2/pokemon/%s'%(name)
response = requests.get(url)
type_data =json.loads(response.text)
typename = type_data['types'][0]['type']['name']

#To get type of pokemon gives double damages to the given pokemon
url = 'https://pokeapi.co/api/v2/type/%s'%(typename)
response = requests.get(url)
type_data =json.loads(response.text)
a = len(type_data['damage_relations']['double_damage_from'])
b = ' '
for i in range(a):
    c = type_data['damage_relations']['double_damage_from'][i]['name']
    b += ', '+c

# 5 pokemons which gives the given pokemon double damage
url = 'https://pokeapi.co/api/v2/type/%s'%(typename)
response = requests.get(url)
type_data =json.loads(response.text)
e = len(type_data['damage_relations']['double_damage_from'])
d = []
for i in range(e):
    d.append(type_data['damage_relations']['double_damage_from'][i]['name'])
for j in d:
    url2 = 'https://pokeapi.co/api/v2/type/%s'%(j)
    response2 = requests.get(url2)
    type_data2 =json.loads(response2.text)
    f = ' '
    for k in range(5):
        g  = type_data2['pokemon'][k]['pokemon']['name']
        f += ', '+g


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    window['-OUTPUT1-'].update('Type ' + typename )
    window['-OUTPUT2-'].update('Double Damage:' + b )
    window['-OUTPUT3-'].update('Pokemons Double Damage:' + f )
    

window.close()
